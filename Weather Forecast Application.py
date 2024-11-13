import requests
import json

api_key = "398e68ec9547b53d5a9caed9b420d902"
city = input("Enter city: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)
data = json.loads(response.text)
print(f"Weather in {city}: {data['weather'][0]['description']}")
print(f"Temperature: {data['main']['temp']}°C")
