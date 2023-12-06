import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/mohinidave")
db = client["Intelligent_Travelling"]

users_collection = db["User"]


def login_user(data):
    email = data.get('email')
    password = data.get('password')

    user_data = users_collection.find_one({'email': email})
    
    if not user_data:
        return {'message': 'User not found'}, 404

    if user_data['password'] == password:
        return {'message': 'Login successful'}, 200,

    else:
        return {'message': 'Invalid credentials'}, 401
