import smtplib, pdb, re
from os import environ
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

NAME = environ.get('NAME')# This could be your actual name
EMAIL_USERNAME: str = environ.get('EMAIL_USERNAME')
EMAIL_PASSWORD: str = environ.get('EMAIL_PASSWORD')
EMAIL_HOST: str = environ.get('EMAIL_HOST')
EMAIL_PORT: int = int(environ.get('EMAIL_PORT'))
EMAIL_USE_TLS:bool = (environ.get('EMAIL_USE_TLS')=='True')
EMAIL_RECIPIENTS: list = re.split(', |,| ',environ.get('EMAIL_RECIPIENTS'))#Using re here to capture any edge cases that may arise from having spaces in our csv values
message = f'''Hello there,
this a test from {EMAIL_USERNAME}. Oooh! Sorry...
'''

SENDER = f'{NAME} <{EMAIL_USERNAME}>'

def send_mail(body: str = message, subject: str = 'Python Sandbox Test', recepients:list = None, sender: str = SENDER, html=None):
    assert isinstance(recepients, list)
    '''This function creates a connection to the SMTP server to send an email
    Args:   body - The text that will be used in the email body
            subject - The email subject
            recepients - A list of the recepients
            sender - The email of the sender
    '''
    message = MIMEMultipart('alternative')
    message['From']= sender
    message['To'] = ', '.join(recepients)
    message['Subject'] = subject
    
    message_text = MIMEText(body, 'plain', 'utf-8')
    message.attach(message_text)
    if html !=None:
        message_html = MIMEText(f'{body} Actually this is HTML', 'html', 'utf-8')
        message.attach(message_html)


    message = message.as_string()
    with smtplib.SMTP(host=EMAIL_HOST, port= EMAIL_PORT) as server:
        server.starttls()
        server.login(user=EMAIL_USERNAME, password=EMAIL_PASSWORD)
        server.sendmail(sender,recepients,message)
        




if __name__ == '__main__':
    send_mail(recepients=EMAIL_RECIPIENTS)