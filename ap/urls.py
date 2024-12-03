from django.urls import path
from ap.views import *
urlpatterns=[
    path('state/',state,name='state'),
]