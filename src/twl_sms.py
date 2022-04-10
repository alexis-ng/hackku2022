import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
def send_sms(phone_number, body):
    account_sid = os.environ[TWILIO_ACCOUNT_SID]
    auth_token = os.environ[TWILIO_AUTH_TOKEN]
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=body,
                        from_='+16076011507',
                        to=phone_number
                    )

    print(message.sid)


