from django.shortcuts import render
import requests
import geocoder


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'account/register.html')


# def course_details(request):
#     URL = requests.get("https://ipinfo.io/")
#     data = URL.json()
#     city = ["New York City", "Philadelphia", "Toronto", "Boston", "Chicago", "Los Angeles", "San Diego", "Dallas",
#             "Houston", "Atlanta", "Miami"]
#     context = []
#
#     if data['city'] in city:
#         context.append({
#             'city': data['city']
#         })
#     else:
#         context.append({
#             'city': "Unknown"
#         })
#     print(data)
#     return render(request, 'course-details.html', {'city_list': context[0]['city']})

def course_details(request):
    g = geocoder.ip('me')
    list_city = ["New York City", "Surat", "Philadelphia", "Toronto", "Boston", "Chicago", "Los Angeles", "San Diego",
                 "Dallas", "Houston", "Atlanta", "Miami"]
    latlng = g.latlng
    city = g.city
    state = g.state
    country = g.country
    context = []
    if city in list_city:
        context.append({
            'city': city
        })
    else:
        context.append({
            'city': "Unknown"
        })
    print(latlng)
    print(city)
    return render(request, 'course-details.html', {'city_list': city})
    # return render(request, 'course-details.html', {'city_list': context[0]['city']})
