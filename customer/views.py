from django.shortcuts import render,redirect
from  django.template import loader
from restaurant.models import foods
from .forms import Loggingin
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model

# Create your views here.


# def login(request):
#     if request.method == "POST":
#        form= Loggingin(request.POST)
          
#        if form.is_valid():
#            form.save()
           
#     else:
#         form=Loggingin()
            
#     return render(request, 'customer/login.html', {'form':form})

def login_view(request):
    form = Loggingin()
    return render(request, 'customer/login.html', {'form': form})