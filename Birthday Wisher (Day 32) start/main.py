import smtplib

my_email = 'nipsalvin@gmail.com'
password = ''

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, 
                        to_addrs='amwaniki.am@gmail.com', 
                        msg='Subject:TEST\n\nThis is a test Email.')
    connection.close()