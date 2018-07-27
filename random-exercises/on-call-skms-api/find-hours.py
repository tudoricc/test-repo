import imp, os
import time
import datetime
from datetime import datetime
from datetime import time
import fileinput
import getpass
import urllib3

#Cause I don't like noise in my terminal..that's why
urllib3.disable_warnings()


SKMS = imp.load_source(
    'SKMS',
    os.path.dirname(os.path.realpath(__file__)) + '/SKMS.py'
)

username = raw_input('Provide the user you need information about: ')
#passkey = '9Bywns7A6p0RQ1kqLGzO2OVUiu'
passkey = getpass.getpass('Enter your API Key from SKMS:  ')

hostname = 'api.skms.adobe.com'

api = SKMS.WebApiClient(username, passkey, hostname)
api.disable_ssl_chain_verification()

user_id = 0
full_name = 'CashMeOutsideHowBoutThat'

#Queue to present data for
queue = raw_input("Please provide your queue: ")

#month we need the data for
month = raw_input("Provide the month you need to do the math for: ")
if int(month):
    if not(int(month) >= 1 and int(month) <= 12):
        print "[ERROR] Month is not in the correct format,it needs to be an integer from 1 to 12"
        exit()


#year = "2017"
year = raw_input("Provide the year you want to look for: ")
if int(year):
    now = datetime.now()

    if not(int(year) > 2000 and int(year) <= now.year) :
        print "[ERROR] Year is not in the correct format"
        exit()
print
print
print

end_time_string = "none"
start_time_string = "none"

#counting for multiple occurences
start_time_array = []
end_time_array = []

#MAGIC Numbers babyyyy
end_time = datetime.strptime('8/18/2008', "%m/%d/%Y")
start_time = datetime.strptime('8/18/2008', "%m/%d/%Y")

print "[INFO] Getting the userd_id and full name information for the adobe_username: " + username

userdao_query = "SELECT user_id,full_name WHERE active=1 AND adobe_username LIKE \'" + username + "%\' PAGE 1, 1000"
param_dict = {"query": userdao_query}

if api.send_request('UserDao', 'search', param_dict) == True:
    response_dict = api.get_response_dictionary()
    if (
        'data' in response_dict and 'results' in response_dict['data'] and
        isinstance(response_dict['data']['results'], list)
    ):
        result_counter = 0
        for row in response_dict['data']['results']:
            result_counter += 1
            print str(result_counter) + ":"
            for field in row:
                print "\t" + str(field) + ": " + str(row[field])
                if str(field) == "user_id":
                    user_id = int(row[field])
                elif str(field) == "full_name":
                    full_name = str(row[field])
    else:
        print "No devices were returned."
        exit()
else:
    print "ERROR:"
    print "   STATUS: " + api.get_response_status()
    print "   TYPE: " + str(api.get_error_type())
    print "   MESSAGE: " + api.get_error_message()
    if 'unable to json decode' in api.get_error_message().lower():
        print "RESPONSE STRING:"
        print api.get_response_string()




queue_id = 0
print "[INFO] Getting the oncall Query ID for the " + str(queue) + " on call QUEUE  where the adobe_username " + username + " is in"
oncall_queue_query = "SELECT on_call_queue_id WHERE full_name LIKE \'%" + str(queue) + "\%' PAGE 1,1000"

oncall_queue_dict = {"query": oncall_queue_query}
if api.send_request('OnCallQueueDao', 'search', oncall_queue_dict) == True:
    response_dict = api.get_response_dictionary()
    if (
        'data' in response_dict and 'results' in response_dict['data'] and
        isinstance(response_dict['data']['results'], list)
    ):
        result_counter = 0
        for row in response_dict['data']['results']:
            result_counter += 1
            print str(result_counter) + ":"
            for field in row:
                print "\t" + str(field) + ": " + str(row[field])
                queue_id = int(row[field])
    else:
        print "No OnCall queue(s) were returned."
        exit()
else:
    print "ERROR:"
    print "   STATUS: " + api.get_response_status()
    print "   TYPE: " + str(api.get_error_type())
    print "   MESSAGE: " + api.get_error_message()
    if 'unable to json decode' in api.get_error_message().lower():
        print "RESPONSE STRING:"
        print api.get_response_string()



print "[INFO] For user " + str(full_name) + " with user_id:"  + str(user_id) + " which is part of the oncall-queue id: " + str(queue_id)
#on_call_queue_schedule = {"query" : "SELECT * WHERE user_id LIKE '37215' AND queue_id LIKE '26'"}
oncall_query_string = "SELECT * WHERE user_id LIKE \'" + str(user_id) + "\' AND on_call_queue_id LIKE \'" + str(queue_id) + "\' AND (start_datetime LIKE \'" + str(year) + "-" + str(month) +"%\' OR end_datetime LIKE \'" + str(year) + "-" + str(month) +"%\') PAGE 1,1000 "



print "[INFO] Here is the information you requested "
on_call_queue_schedule = {"query" : oncall_query_string }
if api.send_request('OnCallDao', 'search', on_call_queue_schedule) == True:
    response_dict = api.get_response_dictionary()
    if (
        'data' in response_dict and 'results' in response_dict['data'] and
        isinstance(response_dict['data']['results'], list)
    ):
        result_counter = 0
        for row in response_dict['data']['results']:
            result_counter += 1
            print str(result_counter) + ":"
            for field in row:
                print "\t" + str(field) + ": " + str(row[field])
                if str(field) == "start_datetime":
                    start_time_array.append(str(datetime.strptime(row[field],"%Y-%m-%d %H:%M:%S")))
                elif str(field) == "end_datetime":
                    end_time_array.append(str(datetime.strptime(row[field],"%Y-%m-%d %H:%M:%S")))


    else:
        print "No Schedules were returned."
        exit()
else:
    print "ERROR:"
    print "   STATUS: " + api.get_response_status()
    print "   TYPE: " + str(api.get_error_type())
    print "   MESSAGE: " + api.get_error_message()
    if 'unable to json decode' in api.get_error_message().lower():
        print "RESPONSE STRING:"
        print api.get_response_string()
#print "here I am to rock you like a hurricaine..boom boom"


hours_number = 0
days_number = 0


for i in range(len(start_time_array)) :

    start_time_string = start_time_array[i]
    end_time_string = end_time_array[i]
    start_time = datetime.strptime(start_time_string,"%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(end_time_string,"%Y-%m-%d %H:%M:%S")
    if end_time.month != start_time.month:

        if end_time.month == int(month):
            print "On call started the month before so recalculating from day 1 to " + str(end_time.day)
            start_time = start_time.replace(month=end_time.month)
            start_time = start_time.replace(day=1)
            start_time = start_time.replace(hour=0)
            start_time = start_time.replace(minute=0)
        else:
            print "On call Ended in another month so calculating only for the month " + str(start_time.month)
            #end_time = datetime.strptime(start_time)
            end_time = end_time.replace(month=start_time.month)
            end_time = end_time.replace(day=31 if end_time.month == '01' or '03' or '05' or '07' or '08' or '10' or '12' else 30)
            end_time = end_time.replace(hour=23)
            end_time = end_time.replace(minute=59)

    time_difference = end_time - start_time

    #print str(time_difference.days) + " saddasdas " +str(time_difference.seconds)
    hours_number += round((int(time_difference.seconds)/3600),2)
    days_number += time_difference.days


print "------------------------------------------"
print "------------------------------------------"
print "------------------------------------------"
print "Total amount of time"
print "------------------------------------------"
print "------------------------------------------"
print "------------------------------------------"

print str(days_number) + " <----- Days"
print str(hours_number) + " <----- Hours"
print "Total number of hours " + str(float(days_number)*24 + float(hours_number))
