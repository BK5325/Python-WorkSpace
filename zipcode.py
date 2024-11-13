from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent ="clcoding")
zipcode = int(input("Enter Zipcode:"))
location = geolocator.geocode(zipcode)
print(f"Zipcode:{zipcode}")
print("Details of Zipcode : ",location)