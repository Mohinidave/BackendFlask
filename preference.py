import pymongo
  
client = pymongo.MongoClient("mongodb://localhost:27017/mohinidave")
db = client["Intelligent_Travelling"]

users_collection = db["preference"]


def preference_info(data):
   
    name=data.get('name')
    email = data.get('email')
    catagories=data.get('catagories')
    
    preference_data = {
        
        'name':name,
        'email': email,
        'categories':catagories
        
        
    }
    users_collection.insert_one(preference_data)

    return {'message': 'Preferences Added Sucessfully'}, 200