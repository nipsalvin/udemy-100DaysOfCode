import os
from dotenv import load_dotenv
from twilio.rest import Client
import smtplib

load_dotenv()

TWILIO_SID = os.getenv('ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('AUTH_TOKEN')
TWILIO_VIRTUAL_NUMBER = os.getenv('TWILIO_VIRTUAL_NUMBER')
TWILIO_VERIFIED_NUMBER = os.getenv('TWILIO_VERIFIED_NUMBER')
EMAIL = 'nipsalvin@gmail.com'
GMAIL_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD')

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
    
    def send_email(self, message):
        self.message = message
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(
                user=EMAIL,
                password=GMAIL_PASSWORD
            )
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs='amwaniki.am@gmail.com',
                msg= self.message
            )
            connection.close()

