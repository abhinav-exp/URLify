from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def registeration(request):
    if request.method == 'POST':
        Uform = MyUserCreationForm(request.POST)
        print(request.POST)
        if Uform.is_valid():
            Uform.save()
        else : 
            #Uform.save()
            print(Uform.errors)
            print("not saved")
            return render(request, "signUp.html", {"form" : Uform})
    return render(request, "signUp.html", {"form" : MyUserCreationForm})

def loggingin(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else :
            return render(request, "logIn.html", {
                "error" : "INVALID USERNAME or PASSWORD"
            })
    return render(request, "logIn.html")