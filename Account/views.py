from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .forms import SignupForm

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login(request,user)
            return redirect("Core:Home")
        else:
            messages.info(request,"Username Or Password Is Not Valid")
            return redirect('Account:login')
        
    else:
        return render(request, 'Account/login.html')


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        

        if form.is_valid():
            form.save()
            return redirect("Core:Home")
        return render(request, 'Account/signup.html', {'form': form})
    else:
        return render(request, 'Account/signup.html', {'form': form})
