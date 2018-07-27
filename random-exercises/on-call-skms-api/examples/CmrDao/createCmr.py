#! /usr/bin/env python
# ---------------------- #
#  SKMS WEB API EXAMPLE  #
#  Object: CmrDao        #
#  Method: createCmr     #
# ---------------------- #
#
# pylint: disable=C0103
import imp, os
SKMS = imp.load_source(
    'SKMS',
    os.path.dirname(os.path.realpath(__file__)) + '/../../SKMS.py'
)
username = 'your_username'
passkey = 'your_passkey'
domain = 'stage.skms.adobe.com'

api = SKMS.WebApiClient(username, passkey, domain)
api.disable_ssl_chain_verification()
param_dict = {
    'save_as_draft': False,                                           # Whether this CMR should be saved as a draft, or submitted
    'priority': 'normal',                                             # The priority of this CMR - can be normal or urgent
    'summary': 'CMR creation via API',                                # A summary of the Change request
#   'update_cmr_id': 123,                                             # The CMR ID of the CMR to update, in the case of updating a draft, or resubmitting a CMR
#   'change_model': 'My Standard Change',                             # The name of the change model (if applicable) that this CMR should be based on
    'function': 'Application',                                        # The Change Type of the CMR
    'change_executor': 'rsteck@adobe.com',                            # The Change Executor of the CMR
#   'supplier': 'Comcast',                                            # The Supplpier who will be performing the change - only applicable if this is a 3rd Party Change
    'notify_users': ['mhandy@adobe.com', 'bnorman@adobe.com'],        # The users who should be notified of this CMR
    'ticket_type': 'TechOps JIRA',                                    # The type of ticket (if applicable) to be associated with this CMR
    'ticket_number': 'APPREQ-12345',                                  # The ticket number associated with the CMR (if applicable)
    'business_justification': 'Business Justification',               # The Business Justification text for this CMR
    'implementation_plan': 'Implementation Plan',                     # The Implementation Plan text for this CMR
    'equipment_needed': 'Equipment Needed',                           # The Equipment Needed text for this CMR
    'back_out_plan': 'Backout Plan',                                  # The Backout Plan text for this CMR
    'customer_toggle': 'specified',                                   # Which customers will be affected by this CMR. Can be 'all', 'specified', or 'unspecified'
    'affected_customers': ['Adobe.com', '1435212'],                   # An array of customer billing IDs or names. This is only used if customer_toggle is 'specified', in which case this parameter is required.
    'affected_service_environments': [                                # An array of dictionaries, each containing 'service', 'environment', 'risk' and 'impact'. Required if save_as_draft is false.
        {
            'service': 1103,                                          # The service can either be the service name (if it is unique) or a service ID
            'environment': 'Site - DA2',                              # The environment can either be the environment name (if it is unique) or an environment ID
            'risk': 'medium',                                         # The risk can be any of the following: 'low', 'medium' or 'high'
            'impact': 'low',                                          # The impact can be any of the following: 'none', 'low', 'medium' or 'high'
        },
        {
            'service': 'Remote Data Collection',
            'environment': 'Site - SJ1',
            'risk': 'low',
            'impact': 'none',
        },
    ],
    'affected_devices': ['appdev1.dmz.ut1', 'appdev2.dmz.ut1'],       # An array of devices which will be affected by this CMR (optional)
    'on_site_assistance_locations': ['SJ1', 'DA2'],                   # An array containing the locations where on-site assistance is required (optional)
    'maintenance_type': 'maintenance_window',                         # The maintenance type for this CMR, can be maintenance_window or internal_change
#   'maintenance_window_id': '1234'                                   # The Maintenance Window ID the CMR should be associated with if you wish to use an existing maintenance window
    'maintenance_window_start_time': '2014-08-13 03:00',              # A string representing when the Maintenance Window will begin in "YYYY-MM-DD HH:MM" format. This parameter is ignored if maintenance_window_id is set
    'maintenance_window_end_time': '2014-08-13 12:00',                # A string representing when the Maintenance Window will end in "YYYY-MM-DD HH:MM" format. This parameter is ignored if maintenance_window_id is set
}
if api.send_request('CmrDao', 'createCmr', param_dict) == True:
    data_dict = api.get_data_dictionary()
    if ('cmr_id' in data_dict):
        print "CMR ID: " + str(data_dict['cmr_id'])
    if ('maintenance_window_id' in data_dict):
        print "Maintenance Window ID: " + str(data_dict['maintenance_window_id'])
else:
    print "ERROR:"
    print "   STATUS: " + api.get_response_status()
    print "   TYPE: " + str(api.get_error_type())
    print "   MESSAGE: " + api.get_error_message()
