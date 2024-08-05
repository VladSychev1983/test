import datetime
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('hello from django!')

def time(request):
    return HttpResponse(f'Time = {datetime.datetime.now().time()}')
