import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_failure_email(pipeline, status, timestamp):
    sender_email = os.getenv("SMTP_SENDER_EMAIL")
    sender_password = os.getenv("SMTP_SENDER_PASSWORD")
    recipient_email = os.getenv("NOTIFY_EMAIL")
    subject = f"Pipeline Failure Notification: {pipeline}"
    body = f"Pipeline: {pipeline}\nStatus: {status}\nTimestamp: {timestamp}\n\nA pipeline has failed. Please check the dashboard for details."

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f"Failure notification sent to {recipient_email}")
    except Exception as e:
        print(f"Error sending email: {e}")
