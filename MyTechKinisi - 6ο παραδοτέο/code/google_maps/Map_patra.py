from my_secrets import ggeocode as GEOCODE_API_KEY # 1
import requests # 2
import json # 3


def get_location_coordinates(location):
    address = location.replace(",", "+")
    # Define the base url
    geo_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GEOCODE_API_KEY}" # 6
    response = requests.get(geo_url) # 7
    content = response.content.decode("utf8") # 8
    geo_js = json.loads(content) # 9
    geo_status = geo_js["status"] # 10

    if geo_status == "OK": # 11
        geo_elements = geo_js["results"][0] # 12
        geometry = geo_elements["geometry"] # 13
        location_coordinates = geometry["location"] # 14
        location_lat = location_coordinates["lat"] # 15
        location_long = location_coordinates["lng"] # 16
        print(f"Long/lat coordinates successfully extracted.") #17
# Run the script
if __name__ == ("__main__"): # 23
    location = "Patra,Greece" # Test string # 24
    loc_lat, loc_long = get_location_coordinates(location=location) #25
    print(loc_lat, loc_long) # 26