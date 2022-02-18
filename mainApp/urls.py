from django.urls import path
from .views import *

urlpatterns = [
    path('register', registeration),
    path('login', loggingin),
    path('inbox', inbox),
    path('<uuid:link>', display_snippet),

]