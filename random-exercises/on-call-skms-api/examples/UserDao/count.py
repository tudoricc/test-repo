#! /usr/bin/env python
"""This is an example of how to call the count method on the UserDao obj"""
# ---------------------- #
#  SKMS WEB API EXAMPLE  #
#  Object: UserDao       #
#  Method: count         #
# ---------------------- #
#
# pylint: disable=C0103
import imp, os
SKMS = imp.load_source(
    'SKMS',
    os.path.dirname(os.path.realpath(__file__)) + '/../../SKMS.py'
)

username = 'username'
passkey = 'passkey'
hostname = 'api.skms.adobe.com'

api = SKMS.WebApiClient(username, passkey, hostname)
api.disable_ssl_chain_verification()
# The following query pulls a count of employees, grouped by their titles.
param_dict = {"query": "SELECT title, COUNT(user_id) AS title_count WHERE active=1 AND title <> '' GROUP BY title ORDER BY title_count ASC"}
if api.send_request('UserDao', 'count', param_dict) == True:
    response_dict = api.get_response_dictionary()
    if (
        'data' in response_dict and 'results' in response_dict['data'] and
        isinstance(response_dict['data']['results'], list)
    ):
        for row in response_dict['data']['results']:
            out_str = ''
            if 'title' in row:
                out_str += "Title: '" + row['title'] + "' "
            if 'title_count' in row:
                out_str += "Count: " + row['title_count']
            print out_str + "\n"
    else:
        print "No titles were returned."
else:
    print "ERROR:"
    print "   STATUS: " + api.get_response_status()
    print "   TYPE: " + str(api.get_error_type())
    print "   MESSAGE: " + api.get_error_message()
    if 'unable to json decode' in api.get_error_message().lower():
        print "RESPONSE STRING:"
        print api.get_response_string()

print "-----------------------------------\n";

api.disable_ssl_chain_verification()
# The following query pulls a count of employees, grouped by building.
param_dict = {"query": "SELECT COUNT(user_id) AS users_in_lehi WHERE active=1 AND building = 'Lehi'"}
if api.send_request('UserDao', 'count', param_dict) == True:
    response_dict = api.get_response_dictionary()
    if (
        'data' in response_dict and 'results' in response_dict['data'] and
        'users_in_lehi' in response_dict['data']['results']
    ):
        print "Users in Lehi: " +  response_dict['data']['results']['users_in_lehi'] + "\n"
    else:
        print "No counts were returned."
else:
    print "ERROR:"
    print "   STATUS: " + api.get_response_status()
    print "   TYPE: " + str(api.get_error_type())
    print "   MESSAGE: " + api.get_error_message()
    if 'unable to json decode' in api.get_error_message().lower():
        print "RESPONSE STRING:"
        print api.get_response_string()
        