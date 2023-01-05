from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.conf import settings
from .aigenerator import *


# Create your views here.

def home(request):
    context = {}

    if request.method == 'POST':
        LandingPageName = request.POST['LandingPageName']
        LandingPageDetails = request.POST['LandingPageDetails']

        context['section1Title'] = getSection1Title(LandingPageDetails)
        context['section1Description'] = getSection1Description(LandingPageName, LandingPageDetails)

        return render(request, 'website/ai-website.html', context)

    return render(request, 'website/index.html', context)


def website(request):
    context = {}
    return render(request, 'website/website.html', context)
