from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('home/',views.home, name="homepage"),
    path('about/',views.about, name="About Us"),
    path('contact/',views.contact, name="Contact")

]

