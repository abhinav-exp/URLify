from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model

# UserCreationForm has 3 field 
# "username", "password1", "password2"
# Meta is overwritten


class MyUserCreationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta : 
        model = User
        fields = ("first_name", "last_name", "username", "password1", "password2")
    
