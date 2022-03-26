from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.urls import reverse_lazy
from .forms import GroupForm
from .models import Group, Gift, Gifter

def home(request):
    return render(request, 'gift_registry/frontpage.html', {})

def create_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('group_success')
    else:
        form = GroupForm()    
    return render(request, 'gift_registry/create_group.html',{'form':form})
    
def group_detail(request,slug):
    group = request.GET.get('event_name','unnamed event')
    event_date = request.GET.get('event_date',None)
    context = {
        'slug':slug,
        'event_name': group,
        'event_date': event_date,
    }
    return render(request, 'gift_registry/group_detail.html', context)

def view_group(request): 
    return render(request, 'gift_registry/view_group.html', {})
