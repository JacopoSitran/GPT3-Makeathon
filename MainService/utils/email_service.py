import email
import imaplib
import smtplib, ssl
from utils.constants import *


def send_message(message):
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


async def process_new_messages(task):
    
    messages = []
    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select('inbox')

    (retcode, messages) = mail.search(None, '(UNSEEN)')
    if retcode == 'OK':
        for num in messages[0].split() :
            typ, data = mail.fetch(num,'(RFC822)')      
            raw_email = data[0][1]
            _typ, _data = mail.store(num,'+FLAGS','\\Seen')
            raw_email_string = raw_email.decode('utf-8')              
            email_message = email.message_from_string(raw_email_string)
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True)
                        result = await task(body.decode('utf-8'))
                        messages.append(result)
                else:
                        continue
    print(messages)
    return messages