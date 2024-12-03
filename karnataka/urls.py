from django.urls import path
from karnataka.views import *
urlpatterns=[
    path('state/',state,name='state'),
]