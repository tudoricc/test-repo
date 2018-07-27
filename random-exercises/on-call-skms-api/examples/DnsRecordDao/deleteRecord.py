#! /usr/bin/env python
# ---------------------- #
#  SKMS WEB API EXAMPLE  #
#  Object: DnsRecordDao  #
#  Method: deleteRecord  #
# ---------------------- #
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
	# DNS Record Information
	"dns_record_id"         : 4,
	"delete_reason"         : "Reason for deleting record",
	"push_immediately"      : True,
	"update_serial"         : True,                
}
if api.send_request("DnsRecordDao", "deleteRecord", param_dict) == True:
    data_dict = api.get_data_dictionary()
    if (
        "dns_record_id" in data_dict
    ):
		print "Deleting DNS Record ID " + str(data_dict["dns_record_id"])
		print "Created Pending Change ID " + str(data_dict["pending_change_id"])
		print "Created Pending Change Batch ID " + str(data_dict["pending_change_batch_id"])
    else:
        print "The DNS record could not be deleted."
else:
    print "ERROR:"
    print "   STATUS: " + api.get_response_status()
    print "   TYPE: " + str(api.get_error_type())
    print "   MESSAGE: " + api.get_error_message()
