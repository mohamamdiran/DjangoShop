from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.views.generic import FormView, ListView
from .forms import SignupForm, ChangePasswordForm
from Product.models import category
from django.contrib.auth import update_session_auth_hash
from .models import Cart, Order
from django.contrib.auth.mixins import LoginRequiredMixin


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


def profile(request):
    var = {'AllCategories':category.objects.all()}
    return render(request, 'Account/profile.html',var)
    
def ChangePassword(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.info(request, "Password Changed")
            return redirect('Account:profile')
        else:
            return render(request, 'Account/change_password.html', {'form': form,'AllCategories':category.objects.all(),})
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'Account/change_password.html', {'form': form,'AllCategories':category.objects.all(),})


class CartList(LoginRequiredMixin, ListView):
    model = Cart
    context_object_name = 'object_list'
