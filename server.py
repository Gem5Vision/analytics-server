from flask import Flask, request, jsonify, abort
from flask_cors import CORS, cross_origin
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# read secret key from .env file
from dotenv import load_dotenv
import os

load_dotenv()

SECRET = os.getenv('SECRET')
print(SECRET)

# domain = 'http://41a5-2601-200-c181-8670-1dd1-c0d1-f0d4-4e64.ngrok.io'
domain = 'http://localhost:5500'

app = Flask(__name__)
""" limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["1 per minute"]
) """
cors = CORS(app, resources={
            r"/*": {"origins": [domain]}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.before_request
def limit_remote_addr():
    # check if header contains secret and if it is correct
    if request.headers.get('Secret') != SECRET:
        abort(403)
    return None
    if not request.headers.get('Origin'):
        abort(403)
    if domain not in request.headers.get('Origin'):
        abort(403)  # Forbidden


@app.route('/get', methods=['GET'])
def get():
    return jsonify({'success': True})


# run the server
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
