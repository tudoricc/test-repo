#! /usr/bin/env python
# ------------------------------- #
#  SKMS WEB API EXAMPLE           #
#  Object: PendingChangeBatchDao  #
#  Method: search                 #
# ------------------------------- #
#
# pylint: disable=C0103
import imp, os
SKMS = imp.load_source(
    'SKMS',
    os.path.dirname(os.path.realpath(__file__)) + '/../../SKMS.py'
)
username = "your_username"
passkey = "your_passkey"
domain = "api.skms.adobe.com"

api = SKMS.WebApiClient(username, passkey, domain)
api.disable_ssl_chain_verification()
param_dict = {"query": "SELECT * WHERE pending_change_batch_id=ID of batch"}
if api.send_request('PendingChangeBatchDao', 'search', param_dict) == True:
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
