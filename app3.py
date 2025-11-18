#created by Minakshi
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data
users = [
    {"id": 1, "name": "Minakshi"},
    {"id": 2, "name": "Ditiya"}
]

# Home route
@app.route('/')
def home():
    return jsonify({"message": "Flask REST API working"})


# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


# GET single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    return jsonify(user) if user else jsonify({"error": "User not found"}), 404


# CREATE new user  (POST)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        "id": users[-1]["id"] + 1 if users else 1,
        "name": data["name"]
    }
    users.append(new_user)
    return jsonify(new_user), 201


# UPDATE user (PUT)
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    user["name"] = data.get("name", user["name"])
    return jsonify(user)


# DELETE user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted"})


if __name__ == "__main__":
    app.run(debug=True)
