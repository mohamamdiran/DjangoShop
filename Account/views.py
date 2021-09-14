from django.shortcuts import render

# Create your views here.


def login(request):
    var = {}
    return render(request, 'Account/login.html',var)