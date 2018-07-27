#! /usr/bin/env python
# ------------------------------- #
#  SKMS WEB API EXAMPLE           #
#  Object: PendingChangeBatchDao  #
#  Method: processBatch           #
# ------------------------------- #
#
# pylint: disable=C0103
import imp, os
SKMS = imp.load_source(
    "SKMS",
    os.path.dirname(os.path.realpath(__file__)) + "/../../SKMS.py"
)
username = "your_username"
passkey = "your_passkey"
domain = "api.skms.adobe.com"

api = SKMS.WebApiClient(username, passkey, domain)
api.disable_ssl_chain_verification()
param_dict = {
	"pending_change_batch_id"	: "ID of batch",
}
if api.send_request("PendingChangeBatchDao", "processBatch", param_dict) == True:
    data_dict = api.get_data_dictionary()
    if (
        'pending_change_batch_id' in data_dict
    ):
		print "Successfully marked Pending Change Batch ID for processing" + str(data_dict['pending_change_batch_id'])
    else:
        print "Unable to mark Pending Change Batch ID for processing."
else:
    print "ERROR:"
    print "   STATUS: " + api.get_response_status()
    print "   TYPE: " + str(api.get_error_type())
    print "   MESSAGE: " + api.get_error_message()
