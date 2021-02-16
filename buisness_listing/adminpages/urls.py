from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('category', views.category, name='category'),
    path('socialplatform', views.socialplatform, name='socialplatform'),
]
