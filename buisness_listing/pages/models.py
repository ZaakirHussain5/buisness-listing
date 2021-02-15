from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class SocialPlatforms(models.Model):
    platform = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(AbstractBaseUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    phonenumber = models.CharField(max_length=10)
    companyName = models.CharField(max_length=50)
    altPhoneNumber = models.CharField(max_length=10)
    address = models.TextField(blank=True)
    photo = models.ImageField(upload_to='')
    about = models.CharField(max_length=255)
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



class listing(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    bannerImage = models.ImageField(upload_to='listing/')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=50)
    website = models.CharField(max_length=50)
    ratings = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    isPublished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class buisness_socials(models.Model):
    listing = models.ForeignKey(listing, on_delete=models.CASCADE)
    platform = models.ForeignKey(SocialPlatforms, on_delete=models.CASCADE)
    link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class buisness_address(models.Model):
    listing = models.ForeignKey(listing, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class buisness_Contact(models.Model):
    listing = models.ForeignKey(listing, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=10)
    altPhoneNumber = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    faxAddress = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Buisness_reviews(models.Model):
    listing = models.ForeignKey(listing, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='')
    review = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



