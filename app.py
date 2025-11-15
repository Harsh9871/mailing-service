import os
from bottle import Bottle, static_file, request, response
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Bottle()

# Import controllers after app creation to avoid circular imports
from controllers.mail_controller import send_mail_route
from utils.rate_limiter import RateLimiter

# Rate limiter instance
rate_limiter = RateLimiter(
    max_requests=5,
    window_ms=60*1000,  # 1 minute
    trusted_ips=os.getenv('TRUSTED_IPS', '').split(',') if os.getenv('TRUSTED_IPS') else []
)

# Serve static files (including your HTML file)
@app.route('/')
def serve_index():
    return static_file('index.html', root='./static')

@app.route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='./static')

# Mail routes with rate limiting
@app.route('/api/mail/send', method='POST')
def send_mail():
    # Apply rate limiting
    client_ip = request.environ.get('REMOTE_ADDR')
    if not rate_limiter.is_allowed(client_ip):
        response.status = 429
        return {'success': False, 'error': 'Too many requests, please try again later.'}
    
    return send_mail_route(request)

if __name__ == "__main__":
    port = int(os.getenv('PORT', 3100))
    print(f"Mailing microservice running on port {port}")
    print(f"Rate limiting: 5 emails/minute for untrusted IPs")
    trusted_ips = os.getenv('TRUSTED_IPS', '').split(',')
    trusted_count = len([ip for ip in trusted_ips if ip])
    print(f"No rate limiting for: localhost{ f' and {trusted_count} trusted IPs' if trusted_count > 0 else ''}")
    
    app.run(host='0.0.0.0', port=port, debug=True, reloader=True)