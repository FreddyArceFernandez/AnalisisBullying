from twilio.rest import Client

account_sid = 'AC54726cbbd7ae316a8d4ee9473e17fb1d'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Hello! This is an editable text message. You are free to change it and write whatever you like.',
    to='whatsapp:+59176456684'
)

print(message.sid)
    
print(message.sid)
#print(message.sid)
#app = Flask(__name__)

#@app.route('/bot', methods=['POST'])
#def mainspaw():

#       msg = request.form.get('Body','').lower()
#       bot_resp=MessagingResponse()#capturar mensaje de whatsapp
#       if 'Hello' in msg:
#           msg.body("Hello my friend")

#if __name__=='__prueba twilio__':
#   app.run(debug=True)