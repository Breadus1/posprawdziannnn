from flask import Flask, request, jsonify

app = Flask(__name__)
user_records = {}
next_user_id = 1

@app.route('/users', methods=['GET'])
def display_all_users():
    return jsonify({user_id: data for user_id, data in user_records.items()})

@app.route('/users/<int:user_id>', methods=['GET'])
def display_single_user(user_id):
    if user_id in user_records:
        return jsonify(user_records[user_id])
    return "User not found", 404

@app.route('/users', methods=['POST'])
def add_user():
    global next_user_id
    user_info = request.json
    user_records[next_user_id] = user_info
    user_records[next_user_id]['id'] = next_user_id
    next_user_id += 1
    return jsonify(user_records[next_user_id - 1]), 201

@app.route('/users/<int:user_id>', methods=['PATCH'])
def modify_user(user_id):
    if user_id in user_records:
        user_updates = request.json
        user_records[user_id].update(user_updates)
        return jsonify(user_records[user_id])
    return "User not found", 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def erase_user(user_id):
    if user_id in user_records:
        del user_records[user_id]
        return '', 204
    return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True)
