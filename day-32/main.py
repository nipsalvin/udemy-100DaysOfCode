# import smtplib

# my_email = 'nipsalvin@gmail.com'
# password = os.environ.get('GMAIL_APP_PASSWORD')

# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs='amwaniki.am@gmail.com', 
#                         msg='Subject:TEST\n\nThis is a test Email.')
#     connection.close()


# import datetime

# now_with_time = datetime.datetime.now()
# now_with_date = now_with_time.date()
# birthday = datetime.datetime(year=1995, day=20, month=1)

# print(birthday.date())
import datetime
import smtplib
import random
import os
from dotenv import load_dotenv

load_dotenv()

day = datetime.datetime.now()
# print(day.weekday())
if day.weekday() == 2:
    with open(file='day-32\quotes.txt', mode='r') as quote_file:
        all_quotes = quote_file.readlines()
        message = random.choice(all_quotes)
        print(message)


    email = os.getenv('MY_EMAIL')
    password = os.environ.get('GMAIL_APP_PASSWORD')

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=email,
                            msg=f'Subject:KEEP GOING\n\n{message} \nThis is sent from python. #100DaysOfCode'
                            )
        connection.close()