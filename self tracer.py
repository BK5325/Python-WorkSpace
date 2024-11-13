import time
import geocoder
import ipinfo

# Set up your IPInfo access token
access_token = 'YOUR_IPINFO_ACCESS_TOKEN'
handler = ipinfo.getHandler(access_token)

def get_location():
    # Get IP-based location
    g = geocoder.ip('me')
    
    if g.latlng:
        print(f"Latitude: {g.latlng[0]}, Longitude: {g.latlng[1]}")
        print(f"City: {g.city}, Country: {g.country}")
        print("IP-based location retrieved successfully.\n")
    
    # Get additional details using IPInfo
    details = handler.getDetails()
    print(f"IP: {details.ip}")
    print(f"City: {details.city}")
    print(f"Region: {details.region}")
    print(f"Country: {details.country}")
    print(f"Coordinates: {details.loc}")
    print(f"Organization: {details.org}\n")

try:
    # Continuously get live location updates
    while True:
        print("Fetching live location...")
        get_location()
        time.sleep(10)  # Wait 10 seconds before updating

except KeyboardInterrupt:
    print("\nStopped live location tracking.")