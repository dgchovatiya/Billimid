from flask import Blueprint, request, jsonify
from app.models.user import User
from app.utils.auth import token_required
from app.utils.helpers import validate_request_data
from bson import ObjectId
from pymongo.errors import PyMongoError
from app import mongo

bp = Blueprint('user', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    try:
        users = list(mongo.db.users.find())
        for user in users:
            user['_id'] = str(user['_id'])
        return jsonify(users), 200
    except PyMongoError:
        return jsonify({'status': 'failure', 'reason': 'Database is not available'}), 500
    except Exception as e:
        return jsonify({'status': 'failure', 'reason': str(e)}), 500

@bp.route('/user', methods=['PUT'])
@token_required
def update_user():
    try:
        data = request.json
        
        # Validate request data
        if not validate_request_data(data):
            return jsonify({'status': 'failure', 'reason': 'Invalid request data'}), 400

        user_id = data.get('user_id')
        if not ObjectId.is_valid(user_id):
            return jsonify({'status': 'failure', 'reason': 'Invalid user_id'}), 400

        # Update user in the database
        updated_user = User.update_user(user_id, data)
        
        if updated_user:
            return jsonify({'status': 'success'}), 200
        else:
            return jsonify({'status': 'failure', 'reason': 'User not found'}), 404

    except PyMongoError:
        return jsonify({'status': 'failure', 'reason': 'Database is not available'}), 500
    except Exception as e:
        return jsonify({'status': 'failure', 'reason': str(e)}), 500