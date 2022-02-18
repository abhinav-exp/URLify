from django.urls import path
from .views import *

urlpatterns = [
    path('register', registeration),
    path('login', loggingin),
    

]