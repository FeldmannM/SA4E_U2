from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory(app.root_path, 'index.html')

@app.route('/wishes', methods=['POST'])
def add_wish():
    data = request.get_json()
    
    # Sende Wunsch an wish_service
    response_wish = requests.post('http://wish_service:5000/wishes', json=data)
    wish_id = response_wish.json()

    return jsonify({"wish_id": wish_id})

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    
    # Sende Benutzername an user_service
    user_data = {"name": data["name"]}
    response_user = requests.post('http://user_service:5001/users', json=user_data)
    
    return jsonify({"user_id": response_user.json()})

@app.route('/status', methods=['POST'])
def add_status():
    data = request.get_json()
    
    # Sende Status an status_service
    status_data = {"status": data["status"]}
    response_status = requests.post('http://status_service:5002/status', json=status_data)
    
    return jsonify({"status_id": response_status.json()})

@app.route('/wishes', methods=['GET'])
def get_wishes():
    response = requests.get('http://wish_service:5000/wishes')
    return jsonify(response.json())

@app.route('/users', methods=['GET'])
def get_users():
    response = requests.get('http://user_service:5001/users')
    return jsonify(response.json())

@app.route('/status', methods=['GET'])
def get_status():
    response = requests.get('http://status_service:5002/status')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
