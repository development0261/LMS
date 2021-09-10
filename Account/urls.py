from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signUp_In/', views.register, name="signUp_In"),
]
