from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.DetailCategory.as_view(), name="DetailCategory"),
]

