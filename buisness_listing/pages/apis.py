from rest_framework import status, permissions, viewsets

from .serializer import *

class userviewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission = [permissions.AllowAny]
    queryset = User.objects.all()


class category_viewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission = [permissions.AllowAny]
    queryset = Category.objects.all()


class socialPlatformsViewset(viewsets.ModelViewSet): 
    serializer_class = SocialPlatformsSerializer
    permission = [permissions.AllowAny]
    queryset = SocialPlatforms.objects.all()



class listingViewset(viewsets.ModelViewSet):
    serializer_class = listingSerializer
    permission = [permissions.AllowAny]
    queryset = listing.objects.all()


class buisness_socialsViewset(viewsets.ModelViewSet):
    serializer_class = buisness_socialsSerializer
    permission = [permissions.AllowAny]
    queryset = buisness_socials.objects.all()


class buisness_addressViewset(viewsets.ModelViewSet):
    serializer_class = buisness_addressSerializer
    permission = [permissions.AllowAny]
    queryset = buisness_socials.objects.all()

class buisness_ContactViewset(viewsets.ModelViewSet):
    serializer_class = buisness_contactSerializer
    permission = [permissions.AllowAny]
    queryset = buisness_Contact.objects.all()

class Buisness_reviewsViewset(viewsets.ModelViewSet):
    serializer_class = buisness_reviewsSerializer
    permission = [permissions.AllowAny]
    queryset = Buisness_reviews.objects.all()

