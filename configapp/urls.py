from django.urls import path
from configapp.views import *

urlpatterns = [
    path('movie_api/', movie_api),
    path('movie_detail/<slug:slug>/', movie_detail),
    # path('ism_api/', ism_api),
]