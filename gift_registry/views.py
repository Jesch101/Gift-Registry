from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.urls import reverse
from django.db import IntegrityError

from .forms import GroupForm
from .models import Group, Gift, Gifter

def home(request):
    return render(request, 'gift_registry/frontpage.html', {})

def create_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            try:
                form.save(commit=True)
            except IntegrityError as e:
                context = {
                    'form':form,
                    'error':True,
                }
                return render(request, 'gift_registry/create_group.html', context)
            context = {
                'name': form.cleaned_data['event_name'],
                'date': form.cleaned_data['event_date'],
                'join_code': form.cleaned_data['join_code']
            }

            return render(request, 'gift_registry/create_group_success.html', context)
    else:
        form = GroupForm()    
    return render(request, 'gift_registry/create_group.html',{'form':form})
    
def group_detail(request):
    return render(request, 'gift_registry/group_detail.html',{})


def view_group(request): 
    return render(request, 'gift_registry/view_group.html', {})
