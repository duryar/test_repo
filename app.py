# This is Flask application
# Example code in starting of script
from flask import Flask, request, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Hello from Flask inside Docker!"

# GET API endpoint - consolidated from routes/get_api.py
@app.route('/api/get', methods=['GET'])
def get_data():
    return jsonify({"message": "This is a GET API endpoint", "status": "success"})

# POST API endpoint - consolidated from routes/post_api.py
@app.route('/api/post', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify({"message": "Data received successfully", "data": data, "status": "success"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
