from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://user_db:27017/benutzer"
mongo = PyMongo(app)
CORS(app)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user = {
        "name": data.get("name")
    }
    user_id = mongo.db.users.insert_one(user).inserted_id
    return jsonify(str(user_id)), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    result = [{"_id": str(u["_id"]), "name": u["name"]} for u in users]
    return jsonify(result)

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    mongo.db.users.delete_one({'_id': ObjectId(user_id)})
    return jsonify({"message": "User deleted successfully!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
