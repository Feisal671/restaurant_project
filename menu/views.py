from django.shortcuts import render

# Create your views here.
from .models import MenuItem

def menu_list(request):
    items = MenuItem.objects.all()
    return render(request, 'menu/menu_list.html',{'items': items})
