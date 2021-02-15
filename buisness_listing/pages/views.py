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

def listings(request):
    return render(request, 'pages/listing.html')

