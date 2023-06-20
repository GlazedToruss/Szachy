from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render(request, 'home.html', {})
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




def login(request):
    return render(request, 'login_page.html')