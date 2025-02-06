from flask import Flask, request, jsonify
import jwt
from datetime import datetime, timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # In production, use a secure secret key

# Make users dict persist between requests
users = {}

@app.route('/client_registeration', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    
    if email in users:
        return jsonify({"message": "Email already Exist"}), 400  # Return 400 for duplicate email
        
    users[email] = {
        "password": data.get('password'),
        "name": data.get('name')
    }
    return jsonify({"message": "User Registered"}), 200

@app.route('/client_login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email not in users or users[email]['password'] != password:
        return jsonify({"message": "Invalid credentials"}), 401

    token = jwt.encode({
        'email': email,
        'exp': datetime.utcnow() + timedelta(hours=24)
    }, app.config['SECRET_KEY'])

    return jsonify({"token": token}), 200

@app.route('/client_logout', methods=['POST'])
def logout():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"message": "No token provided"}), 401

    return jsonify({"message": "Logged out successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True) 