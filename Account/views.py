from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .forms import SignupForm
from Product.models import category

# Create your views here.


def login(request):
    
    var = {
        # Get All Categories For Show In Search Box And ... 
        'AllCategories':category.objects.all(),
    }
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
        return render(request, 'Account/login.html',var)


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        

        if form.is_valid():
            form.save()
            return redirect("Core:Home")
        return render(request, 'Account/signup.html', {'form': form,'AllCategories':category.objects.all()})
    else:
        return render(request, 'Account/signup.html', {'form': form,'AllCategories':category.objects.all()})
