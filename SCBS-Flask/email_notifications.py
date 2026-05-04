import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailNotification:
    """
    Reusable Email Notification Service using Gmail SMTP
    """

    def __init__(self, sender_email, sender_password, smtp_server="smtp.gmail.com", smtp_port=587):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, recipient_email, subject, message_html):
        """
        Send email notification

        :param recipient_email: Receiver email
        :param subject: Email subject
        :param message_html: HTML or plain text message
        :return: True if sent successfully, False otherwise
        """

        try:
            # Create email container
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Attach message body (HTML supported)
            msg.attach(MIMEText(message_html, 'html'))

            # Connect to Gmail SMTP server
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # Secure connection

            # Login to email account
            server.login(self.sender_email, self.sender_password)

            # Send email
            server.send_message(msg)

            # Close connection
            server.quit()

            print(f"Email sent to {recipient_email}")
            return True

        except Exception as e:
            print("EMAIL ERROR:", e)
            return False