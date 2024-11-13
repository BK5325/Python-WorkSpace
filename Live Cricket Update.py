from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from myscore import getMessage

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def reply_with_message():
    
    # Get the incoming message body
    team_name = request.values.get('Body', None)
    print(f'Message Received: {team_name}')
    
    # Get the score message
    message = getMessage(team_name)
    
    # Create a Twilio response
    response = MessagingResponse()
    response.message(message)
    
    # Return the response as a string
    return str(response)

if __name__ == '__main__':
    app.run(debug=True)