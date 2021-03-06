"""LMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Account import views as ac_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ac_view.index,name="index"),
    path('courses/course_details', ac_view.course_details,name="course_details"),
    path('courses/Surat', ac_view.upcoming_course_details_Surat,name="upcoming_course_details_Surat"),
    path('courses/Seattle', ac_view.upcoming_course_details_Seattle,name="upcoming_course_details_Seattle"),
    path('demo', ac_view.demo,name="demo"),
    path('ajax_filter/', ac_view.ajax_filter,name="ajax_filter"),
    path('account/', include('Account.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
