#! /usr/bin/env python
"""This is an example of how to call the search method on the DeviceDao obj"""
# ---------------------- #
#  SKMS WEB API EXAMPLE  #
#  Object: DeviceDao     #
#  Method: search        #
# ---------------------- #
#
# pylint: disable=C0103
import imp, os
SKMS = imp.load_source(
    'SKMS',
    os.path.dirname(os.path.realpath(__file__)) + '/../../SKMS.py'
)
api = SKMS.WebApiClient('username', 'passkey', 'api.skms.adobe.com')
api.disable_ssl_chain_verification()
param_dict = {"query": "SELECT name, model.name, model.model_category.full_name WHERE name LIKE '%b%' PAGE 1, 1000"}
if api.send_request('DeviceDao', 'search', param_dict) == True:
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
