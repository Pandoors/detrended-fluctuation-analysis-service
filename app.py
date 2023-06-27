from flask import Flask, request, jsonify
from dfa_logic import handle_request

app = Flask(__name__)


@app.route('/records', methods=['POST'])
def get_records():
    return handle_request()


if __name__ == '__main__':
    app.run(debug=True, port=5000)
