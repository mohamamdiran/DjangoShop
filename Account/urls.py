from django.contrib.auth import views
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = "Account"


urlpatterns = [
    path("profile/",views.profile, name="profile"),
    path("profile/change-password/", views.ChangePassword, name="change_password"),
    path("profile/cart/", views.cart, name="cart"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/",views.login, name="login"),
    path("signup/",views.signup, name="signup"),
]

