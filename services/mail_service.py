import os
from utils.mailer import create_mail_transporter
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

def send_mail_service(to, subject, text=None, html=None, smtp_config=None):
    if smtp_config is None:
        smtp_config = {}
    
    server = create_mail_transporter(smtp_config)
    
    try:
        # Create message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = smtp_config.get('from', os.getenv('DEFAULT_MAIL_FROM'))
        msg['To'] = to
        
        # Add text and HTML parts
        if text:
            text_part = MIMEText(text, 'plain')
            msg.attach(text_part)
        
        if html:
            html_part = MIMEText(html, 'html')
            msg.attach(html_part)
        
        # Send email
        server.send_message(msg)
        return {'message_id': msg['Message-ID']}
    
    except Exception as e:
        raise Exception(f"Failed to send email: {str(e)}")
    finally:
        try:
            server.quit()
        except:
            pass  # Ignore errors when quitting