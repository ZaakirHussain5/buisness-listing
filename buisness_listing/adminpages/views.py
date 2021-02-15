from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard-en/dashboard.html') 


def category(request):
    return render(request, 'dashboard-en/category.html')


def socialplatform(request):
    return render(request, 'dashboard-en/socialPlatforms.html')


def listings(request):
    return render(request, 'dashboard-en/listing.html')

def buisness_socials(request):
    return render(request, 'dashboard-en/buisness_socials.html')


def buisness_address(request):
    return render(request, 'dashboard-en/buisness_address.html')


def buisness_Contact(request):
    return render(request, 'dashboard-en/buisness_Contact.html')


def Buisness_reviews(request):
    return render(request, 'dashboard-en/Buisness_reviews.html')