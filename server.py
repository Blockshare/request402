import flask
import urllib.request
from status_codes import check_status
import json

#21 imports
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

app = flask.Flask(__name__)
payment = Payment(app, Wallet())
app.debug = True


@app.route("/")
def info():
    return "To check the HTTP status of a website, run: 21 buy url http://www.request402.org/get_status/<www.website.com>"

#get website
@app.route('/get_status/<string:website_url>')
@payment.required(500)
def make_password(website_url = None):
    website_url = website_url
    url = "http://"+website_url

    try:
        #get status code:
        a = urllib.request.urlopen(url)
        status = a.getcode()
        description = check_status(status)
        message = {status : description}
        return json.dumps(message)
    except:
        exception = {"Exception raised" : "Possibly %s doesn't exist" % (url)}
        return json.dumps(exception)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
