from functools import wraps
from flask import request, jsonify
from app import mongo

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Check for Authorization token
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split()[1]
        
        if not token:
            return jsonify({'status': 'failure', 'reason': 'Token is missing'}), 401

        if token != "laurhln7t4gkhlnfsp7ywho_hlsfl":
            return jsonify({'status': 'failure', 'reason': 'Invalid token'}), 401

        # Check for session token
        session_token = request.headers.get('session-token')
        if not session_token or not mongo.db.users.find_one({'session_token': session_token}):
            return jsonify({'status': 'failure', 'reason': 'Invalid session token'}), 401

        return f(*args, **kwargs)
    return decorated