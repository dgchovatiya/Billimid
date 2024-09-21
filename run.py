from app import create_app, mongo
from app.models.user import User
from initial_data import initial_users

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # Check if the users collection is empty
        if mongo.db.users.count_documents({}) == 0:
            for user in initial_users:
                User.create_user(user)
            print("Initial users created successfully!")
        else:
            print("Users collection is not empty. Skipping initial user creation.")

        # Print all users in the database
        users = list(mongo.db.users.find())
        print("Users in the database:")
        for user in users:
            print(f"ID: {user['_id']}, Name: {user['first_name']} {user['last_name']}")

    app.run(debug=True)