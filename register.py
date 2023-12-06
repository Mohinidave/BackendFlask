import pymongo
import bcrypt
import datetime
client = pymongo.MongoClient("mongodb://localhost:27017/mohinidave")
db = client["Intelligent_Travelling"]

users_collection = db["User"]


def register_user(data):
   
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    city = data.get('city')
    signupdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    highest_user = users_collection.find_one(sort=[("user_id", -1)])

    if highest_user:
        new_user_id = highest_user["user_id"] + 1
    else:
        new_user_id = 1

    user_data = {
        'user_id': new_user_id, 
        'name': name,
        'email': email,
        'password': hashed_password,
        'city': city,  
        'signupdate':signupdate
    }
    

    users_collection.insert_one(user_data)
    
    return {'message': 'User registered successfully!'}, 200
def email_exists_in_database(email):
           user =users_collection.find_one({"email": email})
           return user is not None

