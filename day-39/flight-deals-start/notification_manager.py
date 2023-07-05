import os
from dotenv import load_dotenv
from twilio.rest import Client
import smtplib

load_dotenv()

TWILIO_SID = os.getenv('ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('AUTH_TOKEN')
TWILIO_VIRTUAL_NUMBER = os.getenv('TWILIO_VIRTUAL_NUMBER')
TWILIO_VERIFIED_NUMBER = os.getenv('TWILIO_VERIFIED_NUMBER')
MY_EMAIL = os.getenv('MY_EMAIL')
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
    
    def send_email(self, emails , message):
        self.message = message
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(
                user=MY_EMAIL,
                password=GMAIL_PASSWORD
            )
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
            connection.close()

