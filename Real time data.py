from geopy.geocoders import Nominatim

def get_address(place):
    geolocator = Nominatim(user_agent="place_info_app")
    location = geolocator.geocode(place)
    if location:
        return location.address
    else:
        return "Location not found."

# Main program
place = input("Enter place: ")
print(f"\nPlace: {place}")
print("Country Address:", get_address(place))
