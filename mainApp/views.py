from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MyUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Snippet, History
import validators
from datetime import datetime

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

def inbox(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        text = ""
        if request.FILES :
            text = request.FILES['filetext'].read().decode("utf-8") 
            print(str(request.FILES['filetext'].read()))
        else:
            text = request.POST['texttext'].decode("utf-8")
            print(str(request.POST['texttext']))
        user = request.user
        s = Snippet(user = user, text = text)
        s.save()
        return HttpResponse(str(s.link))
    return render(request, "inbox.html")

def display_snippet(request, link):
    s = Snippet.objects.get(link = link)
    ip = ""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    obj = History(snippet = s, ip = ip)
    obj.save()
    if validators.url(s.text):
        return HttpResponseRedirect(s.text)
    else:
        return HttpResponse(str(s))

def list_snippet(request):
    user = request.user
    s = Snippet.objects.all()
    s = s.filter(expiry_time__gte = datetime.now())
    #print(s)
    objs = s.values()
    #print(objs)
    return render(request, "list.html", {
        "objs" : objs,
    })

def edit_history(request, link):
    s = Snippet.objects.get(link = link)
    objs = History.objects.all().filter(snippet = s)
    return render(request, "edit.html", {
        "objs" : objs,
    })