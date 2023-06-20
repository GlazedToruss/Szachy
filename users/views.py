from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render(request, 'home.html', {})
def usr(request):
    return render(request, 'login_page.html')
def register(request):
    form = UserCreationForm()
    context ={'form':form}
    return render(request, 'register_page.html')
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            return redirect('users')
            
    else:
        return render(request, 'login.html')