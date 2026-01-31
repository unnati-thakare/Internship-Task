import requests

API_KEY = "PUT YOUR API KEY HERE"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print("\nWeather Report")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Condition:", data["weather"][0]["description"])
else:
    print("Error: City not found or API issue")
