# BilliMD Assessment

This project implements a Flask-based REST API for user management with MongoDB as the database backend.

## Project Structure

```
BilliMD/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models/
│   │   └── user.py
│   ├── routes/
│   │   └── user_routes.py
│   └── utils/
│       ├── auth.py
│       └── helpers.py
├── initial_data.py
├── requirements.txt
└── run.py
```

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd billiMD
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   On Windows `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory and add the following:
   ```
   MONGO_URI=mongodb://localhost:27017/billiMD
   SECRET_KEY=your-secret-key
   ```

5. Ensure MongoDB is running on your local machine or update the MONGO_URI accordingly.

## Running the Application

1. Start the Flask application:
   ```
   python run.py
   ```

   *This will initialize the database with sample users if the users collection is empty.*

2. The API will be available at `http://localhost:5000`.

## Testing the API

You can test the API using Postman or cURL. Here are the main endpoints:

### GET /users

Retrieves all users.

#### Postman
- Method: GET
- URL: `http://localhost:5000/users`
- Headers: None required

#### cURL
```bash
curl -X GET http://localhost:5000/users
```

### PUT /user
(for particular task PUT method will check whether Bearer token and session-token matches with given sample data)
Updates a user's information. You can get user Id by testing GET request.

#### Postman
- Method: PUT
- URL: `http://localhost:5000/user`
- Headers:
  - Content-Type: application/json
  - Authorization: Bearer laurhln7t4gkhlnfsp7ywho_hlsfl  (Note: Here I used token as given in requested question)
  - session_token: rbvkur79jksfu_shjhu
- Body (raw JSON):
  ```json
  {
    "user_id": "66b3d17ce6d8e2f5b93324d3",
    "first_name": "Miami",
    "password": "billmd124Pass$",
    "updated_datetime": "2024-08-07T22:26:12.111Z"
  }
  ```

#### cURL
```bash
curl -X PUT http://localhost:5000/user \
-H "Content-Type: application/json" \
-H "Authorization: Bearer laurhln7t4gkhlnfsp7ywho_hlsfl" \
-H "session_token: rbvkur79jksfu_shjhu" \
-d '{
  "user_id": "66b3d17ce6d8e2f5b93324d3",
  "first_name": "Miami",
  "password": "billmd124Pass$",
  "updated_datetime": "2024-08-07T22:26:12.111Z"
}'
```

## Postman Collection

For easier testing, you can import the Postman collection provided in this repository. The collection includes pre-configured requests for all available endpoints.

To import the collection:
1. Open Postman
2. Click on "Import" in the top left corner
3. Drag and drop the `API.postman_collection.json` file or browse to select it
4. The collection will be imported and available in your Postman workspace
