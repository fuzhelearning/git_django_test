# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request,'home.html',{'new_item_text':request.POST.get('item_text',"")})

# Create your views here.
