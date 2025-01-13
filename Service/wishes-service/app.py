from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://wish_db:27017/wünsche"
mongo = PyMongo(app)
CORS(app)

@app.route('/wishes', methods=['POST'])
def add_wish():
    data = request.get_json()
    wish = {
        "wish": data.get("wish")
    }
    wish_id = mongo.db.wishes.insert_one(wish).inserted_id
    return jsonify(str(wish_id)), 201

@app.route('/wishes', methods=['GET'])
def get_wishes():
    wishes = mongo.db.wishes.find()
    result = [{"_id": str(w["_id"]), "wish": w["wish"]} for w in wishes]
    return jsonify(result)

@app.route('/wishes/<wish_id>', methods=['DELETE'])
def delete_wish(wish_id):
    mongo.db.wishes.delete_one({'_id': ObjectId(wish_id)})
    return jsonify({"message": "Wish deleted successfully!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
