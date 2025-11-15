import os
import uuid
from utils.mailer import create_mail_transporter
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
import smtplib

def generate_message_id():
    """Generate Message-ID in NodeMailer-style format"""
    # Get domain from environment or use a default
    domain = os.getenv('MAIL_DOMAIN', 'mailingservice.com')
    
    # Generate a UUID like NodeMailer does
    message_id = uuid.uuid4()
    
    # Format exactly like NodeMailer: <uuid@domain>
    return f"<{message_id}@{domain}>"

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
        msg['Date'] = formatdate(localtime=True)
        
        # Generate NodeMailer-style Message-ID
        message_id = generate_message_id()
        msg['Message-ID'] = message_id
        
        # Add text and HTML parts
        if text:
            text_part = MIMEText(text, 'plain')
            msg.attach(text_part)
        
        if html:
            html_part = MIMEText(html, 'html')
            msg.attach(html_part)
        
        # Send email
        server.send_message(msg)
        
        # Return without the angle brackets for consistency with NodeMailer
        clean_message_id = message_id.strip('<>')
        return {'message_id': clean_message_id}
    
    except Exception as e:
        raise Exception(f"Failed to send email: {str(e)}")
    finally:
        try:
            server.quit()
        except:
            pass