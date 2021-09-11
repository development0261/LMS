from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'account/register.html')


def course_details(request):
    URL = requests.get("https://ipinfo.io/")
    data = URL.json()
    city = ["New York City","Seattle", "Philadelphia", "Boston", "Chicago", "Los Angeles", "San Diego", "Dallas", "Houston", "Atlanta", "Miami"]
    context = []
    print(data)
    if data['city'] in city:
        context.append({
            'city' : data['city']
        })
    else:
        context.append({
            'city': "Unknown"
        })
    return render(request, 'course-details.html', {'city_list':context[0]['city']})
