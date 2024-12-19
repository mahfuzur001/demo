from django.urls import path

from .views import *
urlpatterns = [
    path('',signin,name='login'),
    path('',signup,name='login'),
]
