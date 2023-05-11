import datetime
import smtplib
import random

day = datetime.datetime.now()
# print(day.weekday())
if day.weekday() == 2:
    with open(file='day-32\quotes.txt', mode='r') as quote_file:
        all_quotes = quote_file.readlines()
        message = random.choice(all_quotes)
        print(message)


    email = 'nipsalvin@gmail.com'
    password = ''

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs='amwaniki.am@gmail.com',
                            msg=f'Subject:KEEP GOING\n\n{message}. \nThis is sent from python. #100DaysOfCode'
                            )
        connection.close()