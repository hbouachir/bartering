from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def list_users(request):
    return render(request,'users/list_users.html')
