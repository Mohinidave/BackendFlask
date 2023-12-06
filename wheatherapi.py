import requests

def weatherapi(cityname):
  city=cityname

  base_url="https://api.openweathermap.org/data/2.5/weather"
  api_key="981b7c620ea4aa4fb4eb08f8d9b88d65"

  A={
    "q":city,
    "appid":api_key,
    "units":"metric"
    }

  respond=requests.get(base_url,A)
  data=respond.json()
  print(data)
  weather_info = {
    'lon': data['coord']['lon'],
    'lat': data['coord']['lat'],
    'temp': data['main']['temp'],
    'description': data['weather'][0]['description'],
    'name': data['name']
}
  return weather_info

weatherapi("Leh")