#! /usr/bin/env python
# ---------------------- #
#  SKMS WEB API EXAMPLE  #
#  Object: DeviceDao     #
#  Method: updateRecord  #
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
domain = 'api.skms.adobe.com'

api = SKMS.WebApiClient(username, passkey, domain)
api.disable_ssl_chain_verification()
param_dict = {
    # Key value can be a string with the device name, an integer with the device ID,
    # or specified as the serial, asset_id, or asset_tag.tag using a key/value dictionary
    # Example: "key_value": {"serial": "USE943N522"},
    "key_value": "test_api_device2",
    "field_value_arr": {
        # Base Device Information
        "name": "test_api_device1",
        "label": "testapidevice1",
        "device_service": ["Insight - Admin", "SiteCatalyst - Admin - Metrics"],  # Multiple device services can be specified as an array
        "asset_tag": "MAP560",
        "serial": "USE943N522",
        "device_state": "Online",
        "device_state_notes": "Test Device State",
        "environment": "SiteCatalyst - DAL - beta",
        "install_date": "2014-08-14",
        "notes": "Test Notes",
        "ownership": "Owned",
        "model": "ProLiant DL380 G5",
        "vendor_supplier": "HP",

        # Network Settings
        "primary_ip": "16.149.12.17",
        "secondary_ip": "10.10.10.17",
        "ilo_ip": "fd68:d47b:dbf9:c129:5432:ffde:4564:6a3b",
        "ilo_ad_auth": "ABC",
        "mac_addr": "00-1B-78-03-6E-27",
        "int_dns_name": "backtest1.test.omniture.com",
        "ext_dns_name": "test1.test.omniture.com",
        "ad_domain": "TEST",

        # Assignment Information
        # Customer
            # Note: You could also specify a customer name, either simply as "customer" as shown below, or as "customer.name"
            # However, if more than one customer record is found with the same name, an error will occur
            # "customer": "ALLSTATE INSURANCE COMPANY",
        "customer.billing_id": "1437754",
        "assigned_to_user": "mhandy",

        # Hardware Settings
        "disks": "(2) SATA 40GB 7.2k RPM",
        "cpu": "(2) 1 core 1.0GHz, 133MHz FSB, Intel Pentium III",
        "cpu_cores": "2",
        "memory": "4GB",
        "num_attached_storage": "2",
        "num_power_supplies": "2",

        # Location information
        # Location Status - The additional required fields will depend on the specified location status
            # i.e. "In Cage" will require a cage, "In Location" will require a location
        "location_status": "In Rack (Mounted)",
        # Rack - Rack uniqueness is determined based on name, cage.name and cage.location.name, so all 3 need to be specified
        "rack": {
            "name": "103",
            "cage.name": "52200",
            "cage.location.name": "VA5",
        },
        "rack_position": "BACK",
        "rack_unit": "45",
        "location_notes": "Test Location Notes",

        # Operating System Settings
        "operating_system": "Microsoft Windows Server 2003 Enterprise 64 bit",
        "kernel": "5.2.3790 Service Pack 2 Build 3790",

        # Software Versions - multiple software versions can be specified for a device, uniqueness is based on software.name and version
        "software_version": [
            {
                "software.name": "Apache",
                "version": "2.2.6",
            },
            {
                "software.name": "MySQL",
                "version": "5.0.90",
            },
        ],

        # Insight-specific fields
        "insight_dataset": "call center",
        "dop_version": "1.0",
        "dop_path": "/dev/null",
    }
}
if api.send_request('DeviceDao', 'updateRecord', param_dict) == True:
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
