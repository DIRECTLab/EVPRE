import requests


def get_weather_data(lat, lon, weather_api_key):

    params = {"appid": weather_api_key, "lat": str(lat), "lon": str(lon)}
    weatherRequest = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?", params=params)
    weatherResponse = weatherRequest.json()  # Converts into type 'dict'

    # wind_heading = weatherResponse['wind']['deg']
    wind_heading = (weatherResponse.get('wind', {})).get('deg', 0)
    temperature = (weatherResponse.get('main')).get('temp')
    humidity = (weatherResponse.get('main')).get('humidity')
    visibility = weatherResponse.get('visibility')
    wind_speed = (weatherResponse.get('wind')).get('speed')

    weather_dict = {
        "temperature": temperature,
        "humidity": humidity,
        "visibility": visibility,
        "wind_speed": wind_speed,
        "wind_heading": wind_heading

    }

    return weather_dict
