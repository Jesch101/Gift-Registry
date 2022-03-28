from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import DetailView
from django.urls import reverse
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from datetime import date

from .forms import GroupForm, FindGroupForm
from .models import Group, Gift, Gifter

def home(request):
    return render(request, 'gift_registry/frontpage.html', {})

def create_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            try:
                f = form.save()
            except IntegrityError:
                context = {
                    'form':form,
                    'error':True,
                }
                return render(request, 'gift_registry/create_group.html', context)
            return redirect('group_detail',slug=f.slug)
    else:
        form = GroupForm()    
    return render(request, 'gift_registry/create_group.html',{'form':form})
    
def find_group(request):
    queryset = Group.objects.all()
    form = FindGroupForm(request.POST or None)
    context = {
        'form':form
    }
    if request.method == 'POST':
        if form.is_valid():
            try:
                queryset = Group.objects.filter(
                    event_name__exact = form.cleaned_data['event_name'],
                    join_code__exact = form.cleaned_data['join_code']
                    )
                if not queryset or queryset.count() > 1:
                    raise ObjectDoesNotExist
            except:
                context = {
                    'form':form,
                    'error':True
                }
                return render(request, 'gift_registry/view_group.html', context)
            
            context = {
                'form':form,
                'queryset':queryset,
                'slug':queryset[0].slug,
                'foundGroup':True
            }

    return render(request, 'gift_registry/view_group.html', context)


def group_detail(request, slug):
    group = Group.objects.get(slug=slug)
    days_left = group.event_date - date.today()
    if days_left.days < 0:
        time_left = "The event date has passed!"
    elif days_left.days == 0:
        time_left = "Today's the day!"
    else:
        time_left = f"{days_left.days} days left til the event!"

    context = {
        'group':group,
        'time_left':time_left
    }
    return render(request, 'gift_registry/group_detail.html',context)
