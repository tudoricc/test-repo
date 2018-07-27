#! /usr/bin/env python
# ---------------------- #
#  SKMS WEB API EXAMPLE  #
#  Object: DnsRecordDao  #
#  Method: createRecord  #
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
	"source_of_record"      : "TOAD",
	"fqdn"                  : "testing.dev.skms.adobe.com",
	"type"                  : "CNAME",
	"ttl"                   : "900",
	"content"               : "appdev1.dmz.ut1.omniture.com",
	"site"                  : "ALL",
#	"prio"					: "30", // Prio is only valid for MX type records
	"dns_advertisement_map" : {
		"name" : "DEFAULT MAP. Use for most records. Use this map and set the primary_site field in your records to ALL unless you need different DNS responses in different sites. Technically, this map specifies that any record with primary_site = ALL will be advertised in all sites."
	},
	"push_immediately"      : True,
	"update_serial"         : True,                
}
if api.send_request("DnsRecordDao", "createRecord", param_dict) == True:
    data_dict = api.get_data_dictionary()
    if (
        "dns_record_id" in data_dict
    ):
		print "Creating DNS Record ID " + str(data_dict["dns_record_id"])
		print "Created Pending Change ID " + str(data_dict["pending_change_id"])
		print "Created Pending Change Batch ID " + str(data_dict["pending_change_batch_id"])
    else:
        print "The DNS record could not be created."
else:
    print "ERROR:"
    print "   STATUS: " + api.get_response_status()
    print "   TYPE: " + str(api.get_error_type())
    print "   MESSAGE: " + api.get_error_message()
