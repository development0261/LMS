from django.shortcuts import render
import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from geopy.geocoders import Nominatim


# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'account/register.html')


def course_details(request):
    return render(request, 'course-details.html')


@csrf_exempt
def ajax_filter(request):
    if request.method == 'POST':
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')
        locator = Nominatim(user_agent="myGeocoder")
        coordinates = "{}, {}".format(lat, lon)
        location = locator.reverse(coordinates)
        data = list(location)
        first_index = data[0]
        split = first_index.split(",")
        first_add = split[0]
        second_add = split[1]
        print("**********")
        print("**********")
        print(first_index)
        print(first_add)
        print(second_add)
        print("**********")
        print("**********")
        if first_add != "":
            return JsonResponse({'data': first_add,'second_add':second_add})
        else:
            return JsonResponse({'data': "Unknown"})


def upcoming_course_details_Surat(request):
    return render(request, 'upcoming_course_details_Surat.html')


def upcoming_course_details_Seattle(request):
    return render(request, 'upcoming_course_details_Seattle.html')


def demo(request):
    return render(request, 'demo.html')
