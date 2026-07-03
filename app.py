# This is Flask application
from flask import Flask
from routes.get_api import register_get_routes
from routes.post_api import register_post_routes

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask inside Docker!"

# Register API routes
register_get_routes(app)
register_post_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
