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

        context['LandingPageName'] = LandingPageName

        context['section1Title'] = getSection1Title(LandingPageDetails)[0]
        context['section1Description'] = getSection1Description(LandingPageName, LandingPageDetails)

        services = []
        service_titles = get_services(LandingPageDetails)
        for service in service_titles:
            obj = {}
            service_description = get_service_description(service)
            obj['title'] = service
            obj['description'] = service_description
            services.append(obj)

        features = []
        features_titles = get_features(LandingPageDetails)
        for feature in features_titles:
            obj = {}
            feature_description = get_service_description(feature)
            obj['title'] = feature
            obj['description'] = feature_description
            features.append(obj)

        context['service1Title'] = services[0]['title']
        context['service1Description'] = services[0]['description']
        context['service2Title'] = services[1]['title']
        context['service2Description'] = services[1]['description']
        context['service3Title'] = services[2]['title']
        context['service3Description'] = services[2]['description']

        context['section3Title'] = getSection1Title(LandingPageDetails)
        context['section3Description'] = getSection1Description(LandingPageName, LandingPageDetails)

        context['feature1Title'] = features[0]['title']
        context['feature1Description'] = features[0]['description']
        context['feature2Title'] = features[1]['title']
        context['feature2Description'] = features[1]['description']
        context['feature3Title'] = features[2]['title']
        context['feature3Description'] = features[2]['description']

        return render(request, 'website/website1.html', context)

    return render(request, 'website/index.html', context)


def website(request):
    context = {}
    return render(request, 'website/website.html', context)


def website1(request):
    context = {}
    return render(request, 'website/website1.html', context)
