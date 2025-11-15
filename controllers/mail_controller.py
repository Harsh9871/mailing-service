from bottle import response
import services.mail_service as mail_service

def send_mail_route(request):
    try:
        data = request.json
        
        # Validate required fields
        if not data:
            response.status = 400
            return {
                'success': False, 
                'error': 'Request body is required'
            }
        
        if 'to' not in data or 'subject' not in data:
            response.status = 400
            return {
                'success': False, 
                'error': 'Missing required fields: to and subject are required'
            }
        
        to = data.get('to')
        subject = data.get('subject')
        text = data.get('text')
        html = data.get('html')
        smtp_config = data.get('smtp')
        
        result = mail_service.send_mail_service(to, subject, text, html, smtp_config)
        
        return {
            'success': True,
            'messageId': result.get('message_id')
        }
        
    except Exception as error:
        print(f"Error sending mail: {error}")
        response.status = 500
        return {
            'success': False,
            'error': str(error)
        }