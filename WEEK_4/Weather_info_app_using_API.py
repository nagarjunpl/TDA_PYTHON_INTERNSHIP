import requests

def get_weather(city):
    api_key = ""  
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Celsius
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        
        print(f"\n Weather in {city_name}, {country}:")
        print(f" Temperature: {temp}°C")
        print(f" Humidity: {humidity}%")
        print(f" Condition: {description.capitalize()}\n")
    else:
        print("City not found or API error!")

def main():
    print("=== Weather Info App ===")
    while True:
        city = input("Enter city name (or 'exit' to quit): ")
        if city.lower() == "exit":
            print("Goodbye!")
            break
        get_weather(city)

main()
