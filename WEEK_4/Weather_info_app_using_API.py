import requests
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")  # 🔑 Load key from environment
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        print(f"\n📍 Weather in {city.title()}:")
        print(f"🌡 Temperature: {temp}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"☁ Condition: {description.capitalize()}\n")
    else:
        print("❌ City not found or API error!")

def main():
    print("=== Weather Info App ===")
    while True:
        city = input("Enter city name (or 'exit' to quit): ")
        if city.lower() == "exit":
            print("👋 Goodbye!")
            break
        get_weather(city)

main()
