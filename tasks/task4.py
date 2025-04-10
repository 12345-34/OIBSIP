import requests


API_KEY = "ddead733a74ec4a7e1551ead6a8d9cfc"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch weather data for a given city."""
    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}  
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] != 200:
            print("❌ Error:", data["message"])
            return

        
        city_name = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_condition = data["weather"][0]["description"]

        
        print(f"\n🌍 Weather in {city_name}:")
        print(f"🌡 Temperature: {temperature}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"⛅ Condition: {weather_condition.capitalize()}")

    except requests.exceptions.RequestException:
        print("❌ Network error. Please check your connection.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
