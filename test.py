# 192.168.0.89

from geopy.geocoders import Nominatim
locator = Nominatim(user_agent="myGeocoder")
# coordinates = "21.2074274, 72.7924497"
coordinates = "47.7656652, -122.1630365"
location = locator.reverse(coordinates)
data = list(location)
first_index = data[0]
split = first_index.split(",")
print(split[0])
