from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Group, Gift, Gifter

def index(request):
    context = {}
    return render(request, 'base.html', context)

def create_group(request):
    context = {}
    return render(request, 'gift_registry/create_group.html', context)
    
def join_group(request):
    context = {}
    return render(request, 'gift_registry/join_group.html', context)

def group_view(request, id):
    pass