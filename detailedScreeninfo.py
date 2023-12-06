import json

#  Reading json file
with open('IndianJson.json', 'r') as file:
    json_data = json.load(file)

# it is used to extact info of particular city(target_city) from json 
def extract_city_info(json_data, target_city):
    for state in json_data.get('States', []):
        for city in state.get('Cities', []):
            if city.get('CityName') == target_city:
                city_info = {
                    'CityName': city.get('CityName'),
                    'CityImage': city.get('CityImage'),
                    'CityDescription': city.get('CityDescription'),
                    'Category': city.get('Category'),
                    'BestMonthToVisit': city.get('BestMonthToVisit'),
                    'IdealLengthOfTrip': city.get('IdealLengthOfTrip'),
                    'Budgets': city.get('Budget')
                }
                print(city_info)
                return city_info
    print(f"City '{target_city}' not found.")

# Thakur College of science and commerce

# it is used to extact info of particular citie's touristspot from json 
def extract_tourist_spot_info(json_data, target_city, target_spot):
    for state in json_data.get('States', []):
        for city in state.get('Cities', []):
            if city.get('CityName') == target_city:
                for spot in city.get('TouristSpots', []):
                    if spot.get('TouristSpotName') == target_spot:
                        spot_info = {
                            'TouristSpotName': spot.get('TouristSpotName'),
                            'Images': spot.get('Images'),
                            'ReasonOfPopularity': spot.get('ReasonOfPopularity'),
                            'OpeningTime': spot.get('OpeningTime'),
                            'ClosingTime': spot.get('ClosingTime'),
                            'EntryFee': spot.get('EntryFee'),
                            'BestHourToVisit': spot.get('BestHourToVisit'),
                            'Location': spot.get('Location'),
                            'ThingsToDo': spot.get('ThingsToDo'),
                            'NearestRailway': spot.get('Nearestrailway'),
                            'NearestAirport': spot.get('NearestAirport'),
                            'Description': spot.get('Description')
                        }
                        print(spot_info)
                        return
    print(f"Tourist spot '{target_spot}' in city '{target_city}' not found.")




# it is used to extact info of particular state from json 
def extract_state_info(json_data, target_state):
    for state in json_data.get('States', []):
        if state.get('StateName') == target_state:
            state_info = {
                'StateId': state.get('StateId'),
                'StateName': state.get('StateName'),
                'StateImage': state.get('StateImage'),
                'StateDescription': state.get('StateDescription')
            }
            print(state_info)
            return
    print(f"State '{target_state}' not found.")



# it is used to extact info of particular state's cities from json 
def extract_cities_in_state(json_data, target_state):
    for state in json_data.get('States', []):
        if state.get('StateName') == target_state:
            cities = state.get('Cities', [])
            if cities:
                for city in cities:
                    city_info = {
                        'CityId': city.get('CityId'),
                        'CityName': city.get('CityName'),
                        'CityImage': city.get('CityImage'),
                        'CityDescription': city.get('CityDescription'),
                        'BestMonthToVisit': city.get('BestMonthToVisit'),
                        'Budgets': city.get('Budgets'),
                        'Category': city.get('Category'),
                        'IdealLengthOfTrip': city.get('IdealLengthOfTrip')
                    }
                    print(city_info)
                print(len(cities))
                return
            else:
                print(f"No cities found in the state '{target_state}'.")
                return
    print(f"State '{target_state}' not found.")

# it is used to extact info of particular citie's touristspot from json 
def extract_tourist_spots_in_city(json_data, target_city):
    for state in json_data.get('States', []):
        for city in state.get('Cities', []):
            if city.get('CityName') == target_city:
                tourist_spots = city.get('TouristSpots', [])
                if tourist_spots:
                    for spot in tourist_spots:
                        spot_info = {
                            'TouristSpotName': spot.get('TouristSpotName'),
                            'Images': spot.get('Images'),
                            'ReasonOfPopularity': spot.get('ReasonOfPopularity'),
                            'OpeningTime': spot.get('OpeningTime'),
                            'ClosingTime': spot.get('ClosingTime'),
                            'EntryFee': spot.get('EntryFee'),
                            'BestHourToVisit': spot.get('BestHourToVisit'),
                            'Location': spot.get('Location'),
                            'ThingsToDo': spot.get('ThingsToDo'),
                            'NearestRailway': spot.get('NearestRailway'),
                            'NearestAirport': spot.get('NearestAirport'),
                            'Description': spot.get('Description')
                        }
                        print(spot_info)
                        print(len(tourist_spots))
                    return
                else:
                    print(f"No tourist spots found in the city '{target_city}'.")
                    return
    print(f"City '{target_city}' not found.")


