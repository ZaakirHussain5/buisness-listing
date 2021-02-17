from django.shortcuts import render
from listings.models import Category,SocialPlatforms

# Create your views here.
def index(request):
    return render(request, 'pages/index.html',{
        "categories":Category.objects.all(),
    })


def aboutus(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')

def details(request):
    return render(request, 'pages/details.html')

def pricing(request):
    return render(request, 'pages/pricing.html')

def signup(request):
    return render(request, 'pages/signup.html')

def signin(request):
    return render(request, 'pages/signin.html')

def myListings(request):
    return render(request, 'pages/myListings.html')

def editListing(request):
    return render(request, 'pages/editListing.html')

def allListings(request):
    category = request.GET.get("category")
    return render(request, 'pages/allListings.html',{
        "category":category
    })

