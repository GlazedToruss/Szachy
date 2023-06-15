from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):
    return render(request, 'hello.html')

def hello_Maciek(request):
    return render(request, 'hello.html', {'name': 'Maciek'})
#    return HttpResponse('Siemano')