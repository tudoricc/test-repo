import flask
from flask import json

from flask import request
from flask import Flask
import requests
app = Flask(__name__)  # Standard Flask app


@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "Hello, World!"
@app.route("/github",methods =['POST'])
def api_gh_message():
    if request.headers['Content-Type'] == 'application/json':
        my_var = json.dumps(request.json)
        print my_var

        if  'submitted' in request.json['action'] :
            print "SOMETHING WAS SUBMITTED"
            r = requests.get("https://api.github.com/repos/tudoricc/test-repo/pulls/comments/1")
            my_var = r.json()
            print my_var
            print "status is " + r.status_code

        if  'created' in request.json['action'] :
            print "SOMETHING WAS CREATED"
            r = requests.get("https://api.github.com/repos/tudoricc/test-repo/pulls/1/comments")
            print r.json

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=23412)
