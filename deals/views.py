from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def list_deals(request):
    return render(request,'deals/list_deals.html')
