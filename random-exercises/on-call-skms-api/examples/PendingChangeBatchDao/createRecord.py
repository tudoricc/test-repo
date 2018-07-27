#! /usr/bin/env python
# ------------------------------- #
#  SKMS WEB API EXAMPLE           #
#  Object: PendingChangeBatchDao  #
#  Method: createRecord           #
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
	"field_value_arr"		: {
		"name" : "My Batch Name",
		"type" : "1", # See WebAPI guide to know what value to use here. For example, 1=DNS Record
	}
}
if api.send_request("PendingChangeBatchDao", "createRecord", param_dict) == True:
    data_dict = api.get_data_dictionary()
    if (
        'primary_key_arr' in data_dict and
        'pending_change_batch_id' in data_dict['primary_key_arr']
    ):
		print "Created Batch ID " + str(data_dict["primary_key_arr"]['pending_change_batch_id'])
    else:
        print "The Batch could not be created."
else:
    print "ERROR:"
    print "   STATUS: " + api.get_response_status()
    print "   TYPE: " + str(api.get_error_type())
    print "   MESSAGE: " + api.get_error_message()
