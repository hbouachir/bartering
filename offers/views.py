from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def list_offers(request):
    return render(request,'offers/acceuil.html')
