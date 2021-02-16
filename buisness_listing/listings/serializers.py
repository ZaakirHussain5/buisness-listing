from rest_framework import serializers
from .models import User, Category, SocialPlatforms, listing, buisness_socials, buisness_address, buisness_Contact, Buisness_reviews


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class SocialPlatformsSerializer(serializers.ModelSerializer): 
    class Meta:
        model=SocialPlatforms
        fields='__all__'


class listingSerializer(serializers.ModelSerializer):
    class Meta:
        model=listing
        fields='__all__'


class buisness_socialsSerializer(serializers.ModelSerializer):
    class Meta:
        model=buisness_socials
        fields='__all__'


class buisness_addressSerializer(serializers.ModelSerializer):
    class Meta:
        model=buisness_address
        fields='__all__'


class buisness_contactSerializer(serializers.ModelSerializer):
    class Meta:
        model=buisness_Contact
        fields='__all__'


class buisness_reviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Buisness_reviews
        fields='__all__'




