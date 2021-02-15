from django.urls import path, include
from rest_framework import routers

from . import views
from .apis import (userviewset, category_viewset, socialPlatformsViewset, listingViewset, buisness_socialsViewset, buisness_addressViewset, buisness_ContactViewset, Buisness_reviewsViewset)


router = routers.DefaultRouter()

router.register('user', userviewset, 'user')
router.register('category', category_viewset, 'category')
router.register('social_platform', socialPlatformsViewset, 'social_platform')
router.register('listing', listingViewset, 'listing')
router.register('buisness_socials', buisness_socialsViewset, 'buisness_socials')
router.register('business_address', buisness_socialsViewset, 'business_address')
router.register('business_contact', buisness_ContactViewset, 'business_contact')
router.register('business_review', Buisness_reviewsViewset, 'business_review')


urlpatterns = [
    path('apis/', include(router.urls)),
    path('', views.index, name="index"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('advertise', views.advertise, name="advertise"),
    path('contact', views.contact, name="contact"),
    path('details', views.details, name="details"),
    path('pricing', views.pricing, name="pricing"),
    path('listings', views.listings, name="listings"),

]
