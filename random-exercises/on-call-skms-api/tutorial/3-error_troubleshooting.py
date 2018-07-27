#! /usr/bin/env python
#-------------------------------------#
#       SKMS WEB API TUTORIAL #3      #
# Handling and Troubleshooting Errors #
#-------------------------------------#

# See Tutorial #1 for Object Instantiation and Configuration
import SKMS
api = SKMS.WebApiClient("username", "passkey", "api.skms.adobe.com")

# DEBUG MODE
# By enabling Debug Mode all messages returned by the API will include
# additional information including the filename, line number, and backtrace
# from where the message was reported. This information can be useful to the
# Application Development team to assist in troubleshooting.
api.enableDebugMode()

param_dict = { }
if api.sendRequest('ObjectName', 'methodName', param_dict) == True:
	# See Tutorial #2 for Calling Methods and Handling Responses
else:
	# An error occurred while executing the method
	# To see the Error Type, use the getErrorType method:
	print "Error Type: " + api.getErrorType()
	
	# To see the Error Message(s), use the getErrorMessage method. Note: if
	# multiple messages were returned, this will return all messages in a
	# single string.
	print "Error Message: " + api.getErrorMessage()
	
	# Optionally you can loop through all error messages by using the
	# getErrorMessageArray method:
	print "Message:"
	for error_message in api.getErrorMessageDictionary():
		print "-----------------------------"
		print "Message: " + error_message['message']
		# Debug Information - See enableDebugMode() above:
		print "Debug Message: " + error_message['debug_message']
		print "File: " + error_message['file']
		print "Line: " + error_message['line']
		print "Backtrace:"
		for backtrace_data in error_message['backtrace']:
			print "-----------------------------"
			print "- File: " + backtrace_data['file']
			print "- Line: " + backtrace_data['line']
			print "- Class: " + backtrace_data['class']
			print "- Function: " + backtrace_data['function']
	
	# Sometimes, the error is caused due to invalid JSON in the response. To
	# view the entire response string, call the getResponseString method:
	print api.getResponseString()

