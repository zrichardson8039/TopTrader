from django.shortcuts import render
from .forms import RegistrationForm



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
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['first_name']
            username = form.cleaned_data['first_name']
            email = form.cleaned_data['first_name']
            password = form.cleaned_data['first_name']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.save()
            return HttpResponseRedirect('/profile/')
        else:
            return render(request, "registration.html", {})
    else:
        form = RegistrationForm()
        context = {"form": form}
        return render(request, "registration.html", {})