from django.urls import path,include
from rest_framework import routers
from .apis import (userviewset, category_viewset, socialPlatformsViewset, listingViewset, buisness_socialsViewset, buisness_addressViewset, buisness_ContactViewset, Buisness_reviewsViewset)
from .views import signIn


router = routers.DefaultRouter()

router.register('user', userviewset, 'user')
router.register('category', category_viewset, 'category')
router.register('social_platform', socialPlatformsViewset, 'social_platform')
router.register('listing', listingViewset, 'listing')
router.register('buisness_socials', buisness_socialsViewset, 'buisness_socials')
router.register('business_address', buisness_addressViewset, 'business_address')
router.register('business_contact', buisness_ContactViewset, 'business_contact')
router.register('business_review', Buisness_reviewsViewset, 'business_review')

urlpatterns = [
    path('',include(router.urls)),
    path('login',signIn,name="login")
]

