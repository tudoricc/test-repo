#! /usr/bin/env python
#----------------------------------------#
#        SKMS WEB API TUTORIAL #2        #
# Calling Methods and Handling Responses #
#----------------------------------------#

# See Tutorial #1 for Object Instantiation and Configuration
import SKMS
api = SKMS.WebApiClient("username", "passkey", "api.skms.adobe.com")

# Some API methods require parameter data. To see what parameters are required
# for each method, please see the Object Reference page of the Web API Tool
# found within the SKMS. The parameters should be passed as a dictionary.
param_arr = { 'param1': 'Parameter #1 Value', 'param2': 'Parameter #2 Value' }

# To send a request, call the sendRequest method with the object, method, and
# parameter array. True will be returned if the method call was executed
# successfully, and false will be returned if any kind of error occurred.
if api.sendRequest('ObjectName', 'methodName', param_arr) == True:
	# The method was executed successfully.
	# To retrieve the data returned by the method use the getDataDictionary method.
	data = api.getDataDictionary()
	# Some methods will not return any data, others will return one or more
	# key/value pairs found in the data dictionary. For example, if a
	# method were to return data in a key named 'return_val' the following
	# command would print out the value of the 'return_val' data.
	print data['return_val']
	
	# Messages may optionally be returned when a method is executed
	# successfully. To view all messages use the getAllMessageArray method.
	for message in api.getAllMessageDictionary():
		print "Message Type: " + message['type']
		print "Message Text: " + message['message']
	
	# Optionally, you may desire to view the full response text (JSON):
	print api.getResponseString()
else:
	# See Tutorial #3 for Handling and Troubleshooting Errors
