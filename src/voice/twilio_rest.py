from flask import Flask, request, redirect
from twilio.twiml.voice_response import VoiceResponse


app = Flask(__name__)

callers = {
    "+61421179133": "Chetan",
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Say a caller's name, and play an MP3 for them."""

    from_number = request.values.get('From', None)
    if from_number in callers:
        caller = callers[from_number]
    else:
        caller = "Monkey"

    resp = VoiceResponse()
    # Greet the caller by name
    resp.say("Hello " + caller)
    # Play an MP3
    resp.play("http://demo.twilio.com/hellomonkey/monkey.mp3")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
