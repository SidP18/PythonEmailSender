# go over to my gmail account and setup 2 factor authentication
# generate app password
# create a function to send the email
from email.message import EmailMessage #Specifies the sender, password, receiver
from app_info import email_psk
import ssl
import smtplib

email_sender = 'SidharthPrakasan23@gmail.com'
email_psk = email_psk

email_receiver = 'nohol73687@niback.com'

subject = "Python Email Sender"
body = """
Hello, When you get this email, you'll know this python email sender is working!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: # used for login and sending the email
    smtp.login(email_sender, email_psk)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
