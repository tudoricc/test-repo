#! /usr/bin/env python
"""This is an example of how to call the search method on the CsoDao obj"""
# ---------------------- #
#  SKMS WEB API EXAMPLE  #
#  Object: CsoDao   #
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
param_dict = {"query": "SELECT cso_number, started_on, repaired_on, resolved_on WHERE severity = 1 PAGE 1, 250"}
if api.send_request('CsoDao', 'search', param_dict) == True:
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
 