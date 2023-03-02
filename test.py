from flask import Flask, request, send_from_directory

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    # return index.html
    return send_from_directory('.', 'index.html')


if __name__ == '__main__':
    app.run(host='127.2.0.1', port=5000, debug=True)
