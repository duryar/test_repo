from flask import jsonify

def register_get_routes(app):
    @app.route('/api/get', methods=['GET'])
    def get_data():
        return jsonify({"message": "This is a GET API endpoint", "status": "success"})
