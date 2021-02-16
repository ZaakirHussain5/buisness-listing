from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def aboutus(request):
    return render(request, 'pages/about.html')



def advertise(request):
    return render(request, 'pages/advertise.html')


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

