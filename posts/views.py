from django.shortcuts import HttpResponse
from datetime import datetime
# Create your views here.

def main_view(request):
    return HttpResponse('Homework_1')

def hello(request):
    return HttpResponse('Hello! Its my project')

def now_date(request):
    current_dateTime = datetime.now()
    return HttpResponse(current_dateTime)

def goodby(request):
    return HttpResponse('Goodby user!')
