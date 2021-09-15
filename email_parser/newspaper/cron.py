import email
import imaplib
import quopri
# import the logging library
import logging
from datetime import datetime

# Get an instance of a logger
logger = logging.getLogger(__name__)

def fetch_email():
    EMAIL = 'nimra.sadaqat@gmail.com'
    PASSWORD = 'cssdepartmba'
    SERVER = 'imap.gmail.com'
    # connect to the server and go to its inbox
    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select('inbox')

    status, data = mail.search(None, '(FROM "uxlivinglab@dowellresearch.uk")')

    mail_ids = []

    for block in data:
        # b'1 2 3'.split() => [b'1', b'2', b'3']
        mail_ids += block.split()

    for i in mail_ids:
        # the fetch function fetch the email given its id
        # and format that you want the message to be
        status, data = mail.fetch(i, '(RFC822)')

        for response_part in data:
            # so if its a tuple...
            if isinstance(response_part, tuple):
                # we go for the content at its second element
                # skipping the header at the first and the closing
                # at the third
                message = email.message_from_bytes(response_part[1])

                mail_from = message['from']
                mail_subject = message['subject']

                if message.is_multipart():
                    mail_content = ''

                    for part in message.get_payload():
                        # remove quoted-printable encoding
                        unquoted = quopri.decodestring(part.get_payload())
                        mail_content += unquoted.decode('utf-8')
                else:
                    # if the message isn't multipart, just extract it
                    mail_content = message.get_payload()
                # close the connection and logout
                mail.close()
                mail.logout()
                # removing the line break
                page = "".join(line.rstrip("\n") for line in mail_content)
                page = "<table"+page.split('<table', 1)[1]
                page = page.split('</table>', 1)[0]+"</table>"
                new_file=open("newspaper/email.txt",mode="w",encoding="utf-8")
                new_file.write(page)
                new_file.close()
                cron_message = "Cron job was called at "+str(datetime.now())
                logger.info(cron_message)
