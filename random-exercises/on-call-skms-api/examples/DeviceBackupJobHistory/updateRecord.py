#! /usr/bin/env python
# ---------------------- #
#  SKMS WEB API EXAMPLE  #
#  Object: DeviceDao     #
#  Method: updateRecord  #
# ---------------------- #
#
# pylint: disable=C0103
import imp, os, datetime
SKMS = imp.load_source(
    'SKMS',
    os.path.dirname(os.path.realpath(__file__)) + '/../../SKMS.py'
)
username = 'your_username'
passkey = 'your_passkey'
domain = 'api.skms.adobe.com'

api = SKMS.WebApiClient(username, passkey, domain)
api.disable_ssl_chain_verification()
param_dict = {
    # Key value in this instance is the device_backup_job_history_id
    "key_value": "1234",
    "field_value_arr": {
        'current_state': 50,
        'job_end_datetime': datetime.datetime.now().isoformat()
    }
}

if api.send_request('DeviceBackupJobHistoryDao', 'updateRecord', param_dict) == True:
    data_dict = api.get_data_dictionary()
    data_dict = api.get_data_dictionary()
    if (
        'primary_key_arr' in data_dict and
        'device_id' in data_dict['primary_key_arr']
    ):
        print "Successfully updated the device with device_id " + str(data_dict['primary_key_arr']['device_id'])
    else:
        print "The device could not be updated."
else:
    print "ERROR:"
    print "   STATUS: " + api.get_response_status()
    print "   TYPE: " + str(api.get_error_type())
    print "   MESSAGE: " + api.get_error_message()
