from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from dfa_logic import handle_request

app = Flask(__name__)
cors = CORS(app, origins='*', supports_credentials=True, methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/records', methods=['POST'])
@cross_origin()
def get_records():
    return handle_request()


if __name__ == '__main__':
    app.run(debug=True, port=5000)
