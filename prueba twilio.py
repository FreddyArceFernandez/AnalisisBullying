from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

@app.route('/', methods=['POST'])
def mainspaw():
    while True:
        msg = request.form.get('Body')      #capturar mensaje de whatsapp
