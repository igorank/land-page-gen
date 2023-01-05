from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.conf import settings


# Create your views here.

def home(request):
    context = {}

    if request.method == 'POST':
        LandingPageName = request.POST['LandingPageName']
        LandingPageDetails = request.POST['LandingPageDetails']

        print(LandingPageName)
        print(LandingPageDetails)

    return render(request, 'website/index.html', context)
