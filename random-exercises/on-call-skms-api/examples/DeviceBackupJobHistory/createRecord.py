#! /usr/bin/env python
# ---------------------- #
#  SKMS WEB API EXAMPLE  #
#  Object: DeviceDao     #
#  Method: createRecord  #
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
    "field_value_arr": {
        'device_id': 1234,
        'job_start_datetime': datetime.datetime.now().isoformat(),
        'current_state': 0,
        'completion_state': 0,
        'details': 'Job Started'
    }
}

if api.send_request('DeviceBackupJobHistoryDao', 'createRecord', param_dict) == True:
    data_dict = api.get_data_dictionary()
    if (
        'primary_key_arr' in data_dict and
        'device_id' in data_dict['primary_key_arr']
    ):
        print "Successfully created the device with device_id " + str(data_dict['primary_key_arr']['device_id'])
    else:
        print "The device could not be created."
else:
    print "ERROR:"
    print "   STATUS: " + api.get_response_status()
    print "   TYPE: " + str(api.get_error_type())
    print "   MESSAGE: " + api.get_error_message()
