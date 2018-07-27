#! /usr/bin/env python
# ------------------------------- #
#  SKMS WEB API EXAMPLE           #
#  Object: PendingChangeBatchDao  #
#  Method: addPendingChange       #
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
	"pending_change_id"			: "Pending Change ID", # This value would have been returned from a createRecord, updateRecord or deleteRecord API call
	"pending_change_batch_id"	: "Batch ID",
}
if api.send_request("PendingChangeBatchDao", "addPendingChange", param_dict) == True:
    data_dict = api.get_data_dictionary()
    if (
        'pending_change_id' in data_dict and
        'pending_change_batch_id' in data_dict
    ):
		print "Added Pending Change ID " + str(data_dict['pending_change_id']) + " to Pending Change Batch ID " + str(data_dict['pending_change_batch_id'])
    else:
        print "The pending change could not be added to the batch."
else:
    print "ERROR:"
    print "   STATUS: " + api.get_response_status()
    print "   TYPE: " + str(api.get_error_type())
    print "   MESSAGE: " + api.get_error_message()
