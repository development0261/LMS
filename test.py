# 192.168.0.89

from geopy.geocoders import Nominatim
locator = Nominatim(user_agent="myGeocoder")
coordinates = "21.2074274, 72.7924497"
location = locator.reverse(coordinates)

print(location.raw)

#

# g = geocoder.ip('me')
# list_city = ["New York City", "Surat", "Philadelphia", "Toronto", "Boston", "Chicago", "Los Angeles", "San Diego",
#              "Dallas", "Houston", "Atlanta", "Miami"]
# latlng = g.latlng
# city = g.city
# state = g.state
# country = g.country
# context = []
# if city in list_city:
#     context.append({
#         'city': city
#     })
# else:
#     context.append({
#         'city': "Unknown"
#     })
# print(latlng)
# print(city)