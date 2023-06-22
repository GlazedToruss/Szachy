from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
#to jakiś syf ale boję się go usunąć
def usr(request):
    return render(request, 'login_page.html')

def register(request):
    
    form = CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('/users/login')
    context ={'form':form}
    return render(request, 'register_page.html', context)




def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/play/')
        else:
            messages.info(request, 'Username or Passowrd is incorrect :c')
            
    context = {}
    return render(request, 'login_page.html', context)
def logoutt(request):
    logout(request)
    return redirect('/users/login')