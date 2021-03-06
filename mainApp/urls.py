from django.urls import path
from .views import *

urlpatterns = [
    path('register', registeration),
    path('login', loggingin),
    path('', inbox),
    path('<uuid:link>', display_snippet),
    path('list', list_snippet),
    path('<uuid:link>/edit', edit_history),

]