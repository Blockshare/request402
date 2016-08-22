#!/usr/bin/env python3

# Loading Developer Libraries
import flask
import urllib.request
from status_codes import check_status
import json
import socket
import os


from two1.wallet import Wallet
from two1.bitserv.flask import Payment

app = flask.Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

@app.route("/")
def info():
    return "To check the HTTP status of a website, run: 21 buy url http://www.request402.org/get_status/<www.website.com>"


# Get header and status codes of website
@app.route('/get_status/<string:website_url>')
@payment.required(10000)
def get_status(website_url = None):
    website_url = website_url
    url = "http://"+website_url

    try:
        #get status code:
        response = urllib.request.urlopen(url)
        status = response.getcode()
        headers = response.getheaders()[0:8]
        description = check_status(status)
        message = {status : description, 'headers': headers}
        return json.dumps(message)
    except:
        exception = {"Exception raised" : "Possibly %s doesn't exist" % (url)}
        return json.dumps(exception)


# Get IP Address of host
@app.route('/get_ip/<string:website_url>')
@payment.required(10000)
def get_ip(website_url = None):
    website_url = website_url

    try:
        response = socket.gethostbyname(website_url)
        message = {'url': website_url, 'ip_address': response}
        return json.dumps(message)
    except:
        exception = {"Exception raised" : "Possibly http://www.%s doesn't exist" % (website_url)}
        return json.dumps(exception)



if __name__ == "__main__":
    app.run(host="0.0.0.0")
