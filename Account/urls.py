from django.contrib.auth import views
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = "Account"


urlpatterns = [
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/",views.login, name="login"),
]

