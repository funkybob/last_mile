# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python

from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask,jsonify,request, Response,session
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    callers = {
        "+61421179133": "Chetan"
    }
    msg = request.values.get('Body')
    print "msg received " , msg
    from_number = request.values.get('From', None)
    message = callers[from_number] if from_number in callers else "Monkey"

    resp = MessagingResponse()
    resp.message("{}, thanks for the message!".format(message) + " receieved the msg " + str(msg))
    


    return str(resp)



if __name__ == "__main__":
    app.run(debug=True,port=5000)
