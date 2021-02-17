from rest_framework import serializers
from .models import User, Category, SocialPlatforms, listing, buisness_socials, buisness_address, buisness_Contact, Buisness_reviews


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)

        if password is not None :
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr,value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance,attr,value)
        instance.save()
        return instance

    class Meta:
        model=User
        extra_kwargs = {'password':{'write_only':True}}
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




