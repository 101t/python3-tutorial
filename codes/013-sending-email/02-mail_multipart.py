import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HOST = "mail.domain.com"
PORT = 587
USER = "user@domain.com"
PASS = "YOURPASSWORDHERE"

MESSAGE_TEMPLATE = """
<table>
	<tr>
		<td text-align="center">
			<h3>Company Name</h3>
		</td>
	</tr>
	<tr>
		<td>%(message)s</td>
	</tr>
</table>
<br>
<a href="https://domain.com">Company</a> Support Team
"""

def pyMailHTML(subject, from_mail, maillist, message):
	mailserver =  smtplib.SMTP(HOST, PORT)
	mailserver.starttls()
	mailserver.login(USER, PASS)
	for to_mail in maillist:
		msg = MIMEMultipart('related', type="text/html") 
		msg["Subject"] = subject
		msg["From"] = from_mail
		msg["To"] = to_mail
		message = MESSAGE_TEMPLATE % dict(
			message=message,
		)
		part = MIMEText(message, 'html')
		msg.attach(part)
		mailserver.sendmail(from_mail, to_mail, msg.as_string())
	mailserver.quit()


if __name__ == '__main__':
	maillist = ["anotheruser@domain.com", "anotheruser@gmail.com", "anotheruser@live.com"]
	subject = "New HTML Email Test"
	from_mail = USER
	message = "Hello new <b>HTML</b> Email"
	pyMailHTML(subject=subject, from_mail=from_mail, maillist=maillist, message=message)