# This is Flask application
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask inside Docker!"

@app.route('/api/get', methods=['GET'])
def get_data():
    return jsonify({"message": "This is a GET API endpoint", "status": "success"})

@app.route('/api/post', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify({"message": "Data received successfully", "data": data, "status": "success"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
