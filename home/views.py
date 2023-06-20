from django.shortcuts import render, redirect
# Create your views here.

def home_page(request):
    return render(request, 'home_page.html')