from flask import Flask, request, jsonify, abort
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": ["e9aa-207-183-239-54.ngrok.io   "]}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.before_request
def limit_remote_addr():
    print(request.remote_addr)
    print(request.headers.get('Origin'))
    print(list(request.access_route))
    # print domain name
    print(request.headers.get('Host'))
    if request.headers.get('Host') != 'e9aa-207-183-239-54.ngrok.io':
        abort(403)  # Forbidden


@app.route('/get', methods=['GET'])
def get():
    return jsonify({'success': True})


# run the server
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
