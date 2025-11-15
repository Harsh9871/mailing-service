import smtplib
import os

def create_mail_transporter(custom_config=None):
    """Create and return an SMTP connection"""
    if custom_config is None:
        custom_config = {}
    
    host = custom_config.get('host', os.getenv('DEFAULT_MAIL_HOST'))
    port = int(custom_config.get('port', os.getenv('DEFAULT_MAIL_PORT', 587)))
    user = custom_config.get('user', os.getenv('DEFAULT_MAIL_USER'))
    password = custom_config.get('pass', os.getenv('DEFAULT_MAIL_PASS'))
    use_tls = custom_config.get('secure', False)
    
    try:
        if use_tls or port == 465:
            server = smtplib.SMTP_SSL(host, port)
        else:
            server = smtplib.SMTP(host, port)
            if port == 587:  # Typically use STARTTLS on port 587
                server.starttls()
        
        if user and password:
            server.login(user, password)
        
        return server
    except Exception as e:
        raise Exception(f"Failed to create SMTP transporter: {str(e)}")