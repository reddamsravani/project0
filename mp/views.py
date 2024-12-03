from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def state(request):
    return HttpResponse('bhopal is captain of mp')