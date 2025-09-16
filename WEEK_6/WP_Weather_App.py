import requests 

API_KEY = "YOUR API KEY HERE"   # Get it from openweathermap.org

city = input("Enter city name: ")

# API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Get response
response = requests.get(url)

# Convert to JSON (dictionary)
data = response.json()

# Show weather info
if response.status_code == 200:
    print("\nWeather Information ✅")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Farhenate", data["main"]["temp"] * 9/5 + 32, "°F")
    print("Weather:", data["weather"][0]["description"])
    print()
else:
    print("City not found ❌")
