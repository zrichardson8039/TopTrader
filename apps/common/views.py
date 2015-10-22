from django.shortcuts import render


def home(request):
    title = "Welcome | TopTrader"
    context = {
        'title': title
    }

    return render(request, "index.html", context)
