import requests
import geocoder

def get_location(ip_address):
    try:
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        latitude = response['latitude']
        longitude = response['longitude']
        city = response['city']
        region = response['region']
        country = response['country_name']

        print(f'IP Address: {ip_address}')
        print(f'City: {city}')
        print(f'Region: {region}')
        print(f'Country: {country}')
        print(f'Latitude: {latitude}')
        print(f'Longitude: {longitude}')

        # Using geocoder library to get location details
        g = geocoder.reverse(f'{latitude}, {longitude}')
        print(f'Location: {g.addr}')

    except Exception as e:
        print(f'Error: {e}')

ip_address = input("Enter IP Address: ")
get_location(ip_address)
