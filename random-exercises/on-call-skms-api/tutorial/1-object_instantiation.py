#! /usr/bin/env python
# ---------------------------------------- #
#       SKMS WEB API TUTORIAL #1          #
# Object Instantiation and Configuration  #
# ---------------------------------------- #

# In order to use the SkmWebApiClient Class it must be included.
# The following command will include the class file from the parent directory.
import SKMS

# When instantiating the class, the username, password/passkey, and hostname
# of the SKMS endpoint should be specified.
api = SKMS.WebApiClient("username", "passkey", "api.skms.adobe.com")

# After instantiation there are many options that can be set.

# SSL VERIFICATION
# By default the API Client will attempt to verify that the SKMS' SSL
# Certificate is trusted. Some servers are configured with a list of trusted
# intermediate/CA certificates. This list will verify that the SKMS' SSL
# certificate was issued by a trusted source. If your server's configuration
# doesn't have this list of trusted certificates, you can link to a file that
# contains trusted certificates for the SSL verification.
api.setTrustedCertFilePath('/path/to/trusted/cert/file')
# If SSL verification of the SKMS' SSL certificate is not an option, the SSL
# verification can be disabled:
api.disableSslChainVerification()

# REQUEST TIMEOUT
# By default the request timeout is set to 25 seconds. The following call will change the timeout to 5 seconds.
api.setRequestTimeout(5)

# Session Optimization
# By default each request will have it's own session and will require
# authentication and permission checks. By enabling SKMS Session Optimization,
# the API client will store the SKMS Session ID and CSRF Token in a specified
# file and will only require login and permission checks when either the
# session or permission cache have expired. This will improve overall API
# performance. Note: The user running the script must have write access to the
# specified file.
api.enableSkmsSessionOptimization('/path/to/session/info/file')

# DEBUG MODE
# By enabling Debug Mode all messages returned by the API will include
# additional information including the filename, line number, and backtrace
# from where the message was reported. This information can be useful to the
# Application Development team to assist in troubleshooting.
api.enableDebugMode()

# You are now ready to send a request to the SKMS API.
# See Tutorial #2 for how to call API methods.
