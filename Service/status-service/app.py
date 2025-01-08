from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://status_db:27017/status"
mongo = PyMongo(app)
CORS(app)

@app.route('/status', methods=['POST'])
def add_status():
    data = request.get_json()
    status = {
        "status": data.get("status")
    }
    status_id = mongo.db.status.insert_one(status).inserted_id
    return jsonify(str(status_id)), 201

@app.route('/status', methods=['GET'])
def get_status():
    status = mongo.db.status.find()
    result = [{"_id": str(s["_id"]), "status": s["status"]} for s in status]
    return jsonify(result)

@app.route('/status/<status_id>', methods=['PATCH'])
def update_status(status_id):
    new_status = request.json.get('status')
    mongo.db.status.update_one({'_id': ObjectId(status_id)}, {'$set': {'status': new_status}})
    return jsonify({"message": "Status updated successfully!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
