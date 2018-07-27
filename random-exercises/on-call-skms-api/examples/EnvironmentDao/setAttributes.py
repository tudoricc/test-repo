#! /usr/bin/env python
"""This is an example of how to call the setAttributes method on the EnvironmentDao obj"""
# ----------------------- #
#  SKMS WEB API EXAMPLE   #
#  Object: EnvironmentDao #
#  Method: setAttributes  #
# ----------------------- #
#
# pylint: disable=C0103
import imp, os
SKMS = imp.load_source(
    'SKMS',
    os.path.dirname(os.path.realpath(__file__)) + '/../../SKMS.py'
)

username = 'username'
passkey = 'passkey'
hostname = 'api.skms.adobe.com'

api = SKMS.WebApiClient(username, passkey, hostname)
api.disable_ssl_chain_verification()
param_dict = {
    # The attributes you wish to set should be passed as a dictionary:
    'attributes': {
        # To set an attribute, specify an attribute name and value:
        'PUPPET_GIT_REPO': 'techops-core-prod.git',
        # To remove an attribute (and allow for inheritance of that attribute
        # from another CI), set the value to a blank string:
        'COBBLER_PROFILE': '',
    },
    # The environment full name, or full names, that you wish to update with
    # the above attributes should be specified in a list:
    'environments': [
        'SiteCatalyst - SJO - prod',
    ],
}

if api.send_request('EnvironmentDao', 'setAttributes', param_dict) == True:
    data_dict = api.get_data_dictionary()
    if (
        isinstance(data_dict, dict) and 'environments' in data_dict and
        isinstance(data_dict['environments'], dict)
    ):
        print "The following environments were updated:"
        for environment_id in data_dict['environments']:
            print "\t" + data_dict['environments'][environment_id] + " (" + environment_id + ")"
        print ""

    if (
        isinstance(data_dict, dict) and 'attributes' in data_dict and
        isinstance(data_dict['attributes'], dict)
    ):
        print "The following attributes were set:"
        for attribute_name in data_dict['attributes']:
            print "\t" + attribute_name + " = " + data_dict['attributes'][attribute_name]
else:
    print "ERROR:"
    print "   STATUS: " + api.get_response_status()
    print "   TYPE: " + str(api.get_error_type())
    print "   MESSAGE: " + api.get_error_message()

    if 'unable to json decode' in api.get_error_message().lower():
        print "RESPONSE STRING:"
        print api.get_response_string()
