from django.shortcuts import render
from.models import *
from django.core.paginator import Paginator , EmptyPage

# Create your views here.

def Property_view(request):
	return render(request, 'property_list.html')	

def Property_detail(request):
    return  render(request, "property_detail.html")