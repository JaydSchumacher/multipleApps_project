# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'blog_app/index.html')

def new(request):
    return render(request, 'blog_app/new.html')

def show(request):
    return render(request, 'blog_app/show.html' )