#! /usr/bin/env python
"""This is an example of how to call the search method on the DeviceDao obj"""
# ---------------------- #
#  SKMS WEB API EXAMPLE  #
#  Object: DeviceDao     #
#  Method: search        #
# ---------------------- #
#
# pylint: disable=C0103
import imp, os, datetime
SKMS = imp.load_source(
    'SKMS',
    os.path.dirname(os.path.realpath(__file__)) + '/../../SKMS.py'
)
api = SKMS.WebApiClient('username', 'passkey', 'api.skms.adobe.com')
api.disable_ssl_chain_verification()
# get every history item that was started today
param_dict = {"query": "SELECT device_id, device.name, job_start_datetime, job_end_datetime, current_state, completion_state, error_code, data WHERE current_state='0' AND job_start_datetime LIKE '{:s}' PAGE 1, 1000".format(
    datetime.datetime.now().strftime('%Y-%m-%d') + '%'
)}
if api.send_request('DeviceBackupJobHistoryDao', 'search', param_dict) == True:
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
    else:
        print "No devices were returned."
else:
    print "ERROR:"
    print "   STATUS: " + api.get_response_status()
    print "   TYPE: " + str(api.get_error_type())
    print "   MESSAGE: " + api.get_error_message()
