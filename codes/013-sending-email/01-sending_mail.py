import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HOST = "mail.domain.com"
PORT = 587
USER = "user@domain.com"
PASS = "YOURPASSWORDHERE"

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

if __name__ == '__main__':
	maillist = ["anotheruser@domain.com", "anotheruser@gmail.com", "anotheruser@live.com"]
	subject = "New Email Test"
	from_mail = USER
	message = "Hello new Email"
	pyMail(subject=subject, from_mail=from_mail, maillist=maillist, message=message)