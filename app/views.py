import logging
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from app.forms import listForm 
from app.models import list_room
from django.contrib.auth import  login 
from django.contrib.auth import  logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import authenticate
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from .forms import loginForm
from django.contrib import messages

@login_required
def dashboard(request):
     datas = list_room.objects.all( ).order_by('-id')
     context = {
          'datas' : datas
     }
     return render(request ,"dashboard.html", context)


def index(request):
    datas = list_room.objects.all().order_by('-id')
    context = {
         'datas' : datas
    }
    return render(request,"index.html", context)
    

     

def signup(request):
     if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('ulogin')
     else:
        initial_data = {'usrname' : '' , 'password' : ''}
        form = UserCreationForm(initial_data)
    
     return render(request, 'signup.html', {'form': form})     




def ulogin(request):
    form = AuthenticationForm(request , data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('dashboard')
    else:
        initial_data = {'username' :'' , 'password' : ''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'login.html' , {'form' : form})


def ulogout(request):
    logout(request)
    return redirect('index')  
                      

def userlist(request):
    return render(request , 'userlist.html')

@login_required
def listing(request):
     if request.method == "POST":
          form = listForm(request.POST, request.FILES)
          if form.is_valid():
               instance = form.save(commit=False)
               instance.user = request.user
               instance.save()
               return redirect('dashboard')
     else:
      form = listForm()
      return render(request , 'listing.html' , {'form' : form})

def editlist(request, pk_id):
    collect = get_object_or_404(list_room, pk=pk_id , user = request.user)
    if request.method == 'POST':
         form = listForm(request.POST, request.FILES , instance=collect)
         if form.is_valid():
             collect = form.save(commit=False)
             collect.user = request.user
             collect.save()
             return redirect('dashboard')
    else:
      form = listForm(instance=collect)
      context = {
          'form' : form,
          'collect' : collect
      }
    return render(request ,'edit.html', context)

def deletelist(request , pk_id):
 collect = get_object_or_404(list_room , pk = pk_id , user = request.user)
 if request.method == 'POST':
     collect.delete()
     return redirect('dashboard')
 return render(request , 'delete.html',{'collect':collect})
