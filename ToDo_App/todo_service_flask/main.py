from flask import Flask
app = Flask(__name__)

# Setting up a route.
# Route is specified by a URL pattern, an HTTP method, and a function which recieves and handles and HTTP request
# We've set up the root (/) route so that it can be accessed by the URL pattern http://[IP-OR-DOMAIN]:[PORT]/
@app.route('/')
def hello_world():
    return "Hello world!"
