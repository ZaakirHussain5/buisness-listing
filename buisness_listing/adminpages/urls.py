from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('category', views.category, name='category'),
    path('socialplatform', views.socialplatform, name='socialplatformcategory'),
    path('listings', views.listings, name='listings'),
    path('buisness_socials', views.buisness_socials, name='buisness_socials'),
    path('buisness_address', views.buisness_address, name='buisness_address'),
    path('buisness_Contact', views.buisness_Contact, name='buisness_Contact'),
    path('Buisness_reviews', views.Buisness_reviews, name='Buisness_reviews'),
]
