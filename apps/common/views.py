from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



def home(request):
    title = "Welcome | TopTrader"
    context = {
        'title': title
    }
    if request.user.is_authenticated():
        return render(request, "profile.html", {})
    return render(request, "home.html", context)


def registration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        user.save()
        return HttpResponseRedirect('/profile/')
    else:
        context = {"form": form}
        return render(request, "registration.html", context)

def login_request(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        trader = authenticate(username=username, password=password)
        if trader is not None:
            login(request, trader)
            return HttpResponseRedirect('/profile/')
        else:
            return HttpResponseRedirect('/login/')
    else:
        context = {"form": form}
        return render(request, "login.html", context)

def logout_request(request):
    logout(request)
    return HttpResponseRedirect('/')

