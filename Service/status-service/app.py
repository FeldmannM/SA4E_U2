from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://status_db:27017/status"
mongo = PyMongo(app)

@app.route('/status', methods=['POST'])
def add_status():
    data = request.get_json()
    status = {
        "name": data.get("name"),
        "status": data.get("status"),
    }
    status_id = mongo.db.status.insert_one(status).inserted_id
    return jsonify(str(status_id)), 201

@app.route('/status', methods=['GET'])
def get_status():
    status = mongo.db.status.find()
    result = [{"_id": str(s["_id"]), "name": s["name"], "status": s["status"]} for s in status]
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
