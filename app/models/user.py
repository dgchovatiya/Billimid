from app import mongo
from bson import ObjectId
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    @staticmethod
    def create_user(data):
        # Create a new user document
        user = {
            'first_name': data['first_name'],
            'middle_name': data.get('middle_name', ''),
            'last_name': data.get('last_name', ''),
            'password': generate_password_hash(data['password']),
            'phone': data.get('phone', ''),
            'session_token': data.get('session_token', ''),
            'created_datetime': datetime.utcnow(),
            'updated_datetime': datetime.utcnow()
        }
        result = mongo.db.users.insert_one(user)
        return result.inserted_id

    @staticmethod
    def update_user(user_id, data):
        # Update an existing user document
        user = mongo.db.users.find_one_and_update(
            {'_id': ObjectId(user_id)},
            {'$set': {
                'first_name': data['first_name'],
                'password': generate_password_hash(data['password']),
                'updated_datetime': datetime.utcnow()
            }},
            return_document=True
        )
        return user