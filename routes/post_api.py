from flask import request, jsonify

def register_post_routes(app):
    @app.route('/api/post', methods=['POST'])
    def post_data():
        data = request.get_json()
        return jsonify({"message": "Data received successfully", "data": data, "status": "success"})
