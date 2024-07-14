from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to reeleese.net"

@app.route('/api', methods=['GET'])
def api():
    return jsonify({"message": "This is your API response"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
