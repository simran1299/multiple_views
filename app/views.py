from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def propose(request):
    return HttpResponse('<marquee> I Love u </marquee>')

def rejection(request):
    return HttpResponse('<h1> NO </h1>')

def multiple(request):
    return HttpResponse('multiple_views')