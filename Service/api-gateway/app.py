from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory(app.root_path, 'index.html')

@app.route('/wishes', methods=['POST', 'GET'])
def proxy_wishes():
    if request.method == 'POST':
        response = requests.post('http://wish_service:5000/wishes', json=request.get_json())
    else:
        response = requests.get('http://wish_service:5000/wishes')
    return jsonify(response.json())

@app.route('/users', methods=['POST', 'GET'])
def proxy_users():
    if request.method == 'POST':
        response = requests.post('http://user_service:5001/users', json=request.get_json())
    else:
        response = requests.get('http://user_service:5001/users')
    return jsonify(response.json())

@app.route('/status', methods=['POST', 'GET'])
def proxy_status():
    if request.method == 'POST':
        response = requests.post('http://status_service:5002/status', json=request.get_json())
    else:
        response = requests.get('http://status_service:5002/status')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
