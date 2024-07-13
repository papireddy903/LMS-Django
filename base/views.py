from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.views import View 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 


# Create your views here.

class loginUser(View):
    def get(self,request):
        login_form = LoginForm()
        return render(request, "login.html",{"form":login_form})
    
    def post(self,request):
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password) 

            if user is not None:
                login(request, user) 
                messages.info(request, f"You are now logged in {username}.")
                return redirect('/')
            else:
                messages.error(request, f"Invalid Username or Password")
        else:
            messages.error(request, "Invalid Username or Password") 
        


class logoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('/')
        # logout(request, user)



class Home(View):
    def get(self, request):
        return render(request, "home.html", {"user": request.user})