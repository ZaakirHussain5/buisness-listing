from django.urls import path, include
from rest_framework import routers

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('advertise', views.advertise, name="advertise"),
    path('contact', views.contact, name="contact"),
    path('details', views.details, name="details"),
    path('pricing', views.pricing, name="pricing"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('myListings', views.myListings, name="myListings"),
    path('editListing', views.editListing, name="editListing"),

]
