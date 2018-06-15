from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from models import Item

def home_page(request):
    item=Item()
    item.text=request.POST.get('item_text','')
    item.save()

    return render(request,'home.html',{'new_item_text':item.text})