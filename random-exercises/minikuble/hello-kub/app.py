from flask import Flask
from redis import Redis
import os
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Container World! I have been seen times.\n' 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
