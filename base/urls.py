from django.urls import path 
from . import views

urlpatterns = [
    path("login/", views.loginUser.as_view(), name="login"),
    path("logout/", views.logoutUser.as_view(), name="logout"),
    path("",views.Home.as_view(), name="home"),
]