import pymongo
  
client = pymongo.MongoClient("mongodb://localhost:27017/mohinidave")
db = client["Intelligent_Travelling"]

users_collection = db["feedback"]


def feedback_info(data):
   
    
    email = data.get('email')
    comment=data.get('comment')
    
    feedback_data = {
        
        'email': email,
        'comment':comment,
        
        
    }
    users_collection.insert_one(feedback_data)

    return {'message': 'Feedback inserted Successfully'}, 200