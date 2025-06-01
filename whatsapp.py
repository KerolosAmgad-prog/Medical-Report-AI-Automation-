# whatsapp_twilio.py
from twilio.rest import Client


def send_whatsapp(receiver_phone, message, media_url=None):

    # Twilio credentials
    sid = 'AC65764bdc8f39c0e8902bbe6f0f117ff6'  # Replace with your Twilio Account SID
    auth_token = '552cc2976e5460e3a1891c22e41347dd'  # Replace with your Twilio Auth Token
    client = Client(sid, auth_token)

    try:
        # Send the WhatsApp message
        message = client.messages.create(
            to=f'whatsapp:{receiver_phone}',  # Recipient's number in international format
            from_='whatsapp:+14155238886',  # Twilio's sandbox number
            body=message,  # Message body
            media_url=[media_url] if media_url else None  # Attach the file if provided
        )
        print(f"WhatsApp message sent successfully! Message SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {e}")