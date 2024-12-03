from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def state(request):
    return HttpResponse('lucknow is captain of up')
