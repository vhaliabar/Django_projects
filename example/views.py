from django.shortcuts import render
from django.http import HttpResponse

from .tasks import sleepy
# Create your views here.

def index(request):
    sleepy(5)
    return HttpResponse('<h1>THE TASK IS DONE</h1>')