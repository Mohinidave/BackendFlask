from flask_bcrypt import Bcrypt
from flask import Flask, request, jsonify, session
from register import *
from login import *
from reset_password import *
from OTP_validation import *
from change_password import *
from preference import *
from feedback import *
from flask import Flask, session, request
from flask_session import Session
from pymongo import MongoClient
from Dashboard import CITY_IMAGE_10 , SPOT_IMAGE_10, STATE_IMAGE_10,UT_IMAGE_10,BEST_SELLER_10
from FetchUserName import fetch_user_name
from detailedScreeninfo import extract_city_info,extract_cities_in_state,extract_state_info,extract_tourist_spot_info,extract_tourist_spots_in_city
import json
from wheatherapi import weatherapi
with open('IndianJson.json', 'r') as file:
    json_data = json.load(file)


emaillist=[]

app = Flask(__name__)


app.config['PERMANENT_SESSION_LIFETIME'] = 3600
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
all_the_tourist_spot = None
days = 0


@app.route('/register', methods=['GET','POST'])
def register_route():
    data = request.get_json()
    email = data.get('email')

    # Initialize emaillist from session
    emaillist = session.get('emaillist', [])

    # Append the new email to the emaillist
    emaillist.append(email)

    # Store the updated emaillist in the session
    session['emaillist'] = emaillist
    print(emaillist)
    print(session)

    response_data, status = register_user(data)
    return jsonify(response_data), status
       





@app.route('/login', methods=['POST'])
def login_route():
    data = request.get_json()
    email = data.get('email')
    sessionemaillist = session.get('emaillist', [])
    print(sessionemaillist)
     
    if email in sessionemaillist:
        response_data, status = login_user(data)
        return response_data
    else:
        error_message = "Invalid email address"
        return jsonify({"error": error_message}), 400 


@app.route('/send_otp', methods=['POST'])
def send_otp_route():
    try:
        data = request.get_json()
        email = data.get('email')
        if not email:
            return jsonify({'error': 'Email address is required'}), 400
        if send_otp_email(email):
            return jsonify({'message': 'OTP sent successfully'})
        else:
            return jsonify({'error': 'Failed to send OTP'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/emailverification', methods=['POST'])
def emailverification_route():
    try:
        data = request.get_json()
        email = data.get('email')
        
        if email_exists_in_database(email):
           if send_otp_email(email) : 
            return jsonify({'message': 'OTP sent successfully'}), 200
        else:
            return jsonify({'message': 'Email does not exist'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/validate_otp', methods=['POST'])
def validate_otp_route():
    try:
        data = request.get_json()
        email = data.get('email')
        entered_otp = data.get('otp')

        if  not entered_otp:
            return jsonify({'error': 'OTP are required'}), 400
        print(f"Received email: {email}, OTP: {entered_otp}")
        if validate_otp(email, entered_otp):
            return jsonify({'message': 'OTP is valid'})
           
        else:
            return jsonify({'error': 'Invalid OTP'}), 400
           
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/reset_password', methods=['POST'])
def change_password_route():
    try:
        data = request.get_json()
        print(data)
        email = data['fdata']['email']
        
        print(email)
        newpassword= data['fdata']['newpassword']
        

        result = change_password(email, newpassword)
        return jsonify(result)
    except Exception as e:
        return jsonify({'message': f'An error occurred: {str(e)}'}), 500

@app.route('/prefernce', methods=['POST'])
def preference_route():
    # Assuming you're using Flask's session to store the user's email
    data = request.get_json()
    email =data.get('email')
    # sessionemail=session.get('email')
    sessionemaillist = session.get('emaillist', [])
    print(sessionemaillist)
    
    if email in sessionemaillist:
      response_data, status = preference_info(data)
      return jsonify(response_data), status
    


@app.route('/image_to_dashboard', methods=['GET'])
def image_to_dashboard():
    try:
        if session['email']:
            user_email = session['email']
            username = fetch_user_name(user_email)
    except Exception as e:
        username = "Traveller"
    return jsonify({
        "USERNAME": username,
        "BEST_SELLER_10": BEST_SELLER_10,
        'SPOT_IMAGE_10': SPOT_IMAGE_10,
        'CITY_IMAGE_10': CITY_IMAGE_10,
        'STATE_IMAGE_10': STATE_IMAGE_10,
        'UT_IMAGE_3': UT_IMAGE_10
    })
@app.route('/temperature_city',methods=['GET'])
def temperature_city():
     city = request.args.get('city')
     temp_info=weatherapi(city)
     print(temp_info)
     return jsonify(temp_info)
     
     
     
@app.route('/city_information', methods=['GET'])
def city_information():
    try:
        city = request.args.get('city')
        print("city",city)
        city_info=extract_city_info(json_data, city)
        print(city_info)
        return jsonify(city_info)
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": "Internal Server Error"}), 500
    
@app.route('/feedback', methods=['GET','POST'])
def feedback_route():
        data = request.get_json()
        response_data, status = feedback_info(data)
        return jsonify(response_data), status

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
