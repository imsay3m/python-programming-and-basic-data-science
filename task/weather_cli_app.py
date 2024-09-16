import environ
import requests

env = environ.Env()
environ.Env.read_env()

OPENCAGE_API_KEY = env("OPENCAGE_KEY")
OPENWEATHER_API_KEY = env("OPENWEATHER_KEY")


def get_latitude_longitude(city):
    try:
        response = requests.get(
            f"https://api.opencagedata.com/geocode/v1/json?q={city}&key={OPENCAGE_API_KEY}"
        )
        response.raise_for_status()
        data = response.json()

        if data["results"]:
            lat = data["results"][0]["geometry"]["lat"]
            lon = data["results"][0]["geometry"]["lng"]
            return lat, lon
        else:
            print("City not found!")
            return None, None
    except requests.exceptions.Timeout:
        print(f"Timeout error: {requests.exceptions.Timeout}")
    except requests.exceptions.RequestException:
        print(f"Error occurred: {requests.exceptions.RequestException}")
    return None, None


def get_current_weather(lat, lon):
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric"
        )
        response.raise_for_status()
        data = response.json()

        if data:
            weather_description = data["weather"][0]["description"].title()
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            min_temperature = data["main"]["temp_min"]
            max_temperature = data["main"]["temp_max"]
            wind_speed = data["wind"]["speed"]

            print(
                f"Weather: {weather_description}\n"
                f"Temperature: {temperature}°C\n"
                f"Feels Like: {feels_like}°C\n"
                f"Humidity: {humidity}%\n"
                f"Minimum Temperature: {min_temperature}°C\n"
                f"Maximum Temperature: {max_temperature}°C\n"
                f"Wind Speed: {wind_speed}m/s"
            )
        else:
            print("Weather data not found!")
    except requests.exceptions.RequestException:
        print(f"Error occurred: {requests.exceptions.RequestException}")
    except requests.exceptions.Timeout:
        print(f"Timeout error: {requests.exceptions.Timeout}")


city = input("Enter city name: ")
lat, lon = get_latitude_longitude(city)

if lat is not None and lon is not None:
    get_current_weather(lat, lon)
else:
    print("Unable to retrieve latitude and longitude for the city.")
