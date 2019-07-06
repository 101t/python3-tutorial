import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HOST = "mail.example.com"
PORT = 587
USER = "user@example.com"
PASS = "123456"

MESSAGE_TEMPLATE = """From: Company Support Team <%(from_mail)s>
To: Dear Customer <%(to_mail)s>
Subject: %(subject)s

%(message)s
"""

def pyMail(subject, from_mail, maillist, message):
	mailserver =  smtplib.SMTP(HOST, PORT)
	mailserver.starttls()
	mailserver.login(USER, PASS)
	for to_mail in maillist:
		message = MESSAGE_TEMPLATE % dict(
			from_mail=from_mail,
			to_mail=to_mail,
			subject=subject,
			message=message,
		)
		mailserver.sendmail(from_mail, to_mail, message.encode("utf8"))
	mailserver.close()

"""
if __name__ == '__main__':
	maillist = ["anotheruser@domain.com", "anotheruseralso@domain.com", "tarik@example.com"]
	subject = "New Email Test"
	from_mail = USER
	message = "Hello new Email"
	pyMail(subject=subject, from_mail=from_mail, maillist=maillist, message=message)
"""