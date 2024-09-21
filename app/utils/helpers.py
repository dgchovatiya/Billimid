from datetime import datetime

def validate_request_data(data):
    # Check if all required fields are present
    required_fields = ['user_id', 'first_name', 'password', 'updated_datetime']
    if not all(field in data for field in required_fields):
        return False
    
    # Validate the datetime format
    try:
        datetime.fromisoformat(data['updated_datetime'].replace('Z', '+00:00'))
    except ValueError:
        return False
    
    return True