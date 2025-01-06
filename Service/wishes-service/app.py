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
        "name": data.get("name"),
        "wish": data.get("wish"),
        "status": "Formuliert"
    }
    wish_id = mongo.db.wishes.insert_one(wish).inserted_id
    return jsonify(str(wish_id)), 201

@app.route('/wishes', methods=['GET'])
def get_wishes():
    wishes = mongo.db.wishes.find()
    result = [{"_id": str(w["_id"]), "name": w["name"], "wish": w["wish"], "status": w["status"]} for w in wishes]
    return jsonify(result)

@app.route('/wishes/<wish_id>', methods=['PATCH'])
def update_wish_status(wish_id):
    new_status = request.json.get('status')
    mongo.db.wishes.update_one({'_id': ObjectId(wish_id)}, {'$set': {'status': new_status}})
    return jsonify({"message": "Status updated successfully!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
