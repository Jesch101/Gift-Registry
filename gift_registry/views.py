from pickle import NONE
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.urls import reverse
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from datetime import date
from django.http import Http404, HttpResponseRedirect

from .forms import GroupForm, FindGroupForm, AddGiftForm, GifterForm, ClaimedForm
from .models import Group, Gift, Gifter
from .serializers import GroupSerializer, GiftSerializer, GifterSerializer

from rest_framework import viewsets
from rest_framework import permissions

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
        'form':form,
        'access':False
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
                    'error':True,
                    'access':False
                }
                return render(request, 'gift_registry/view_group.html', context)
            
            context = {
                'form':form,
                'queryset':queryset,
                'slug':queryset[0].slug,
                'foundGroup':True,
                'access':True
            }

    return render(request, 'gift_registry/view_group.html', context)

def get_referer(request):
    '''
    Prevents users from being able to try to access any gift page without
    getting the link from the join code form
    '''
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return None
    return referer

def group_detail(request, slug):
    if not get_referer(request):
        raise Http404
    
    group = Group.objects.get(slug=slug)

    days_left = group.event_date - date.today()
    if days_left.days < 0:
        time_left = "The event date has passed!"
    elif days_left.days == 0:
        time_left = "Today's the day!"
    else:
        time_left = f"{days_left.days} days left til the event!"

    gifts = Gift.objects.filter(group=group)
    form = GifterForm(request.POST or None)
    

    if request.method == "POST":
        if form.is_valid():
            f = form.save(commit=False)
            f.group = group
            f.gift = Gift.objects.get(
                group=group,
                title__exact=request.POST['gift'],
                reciever__exact=request.POST['reciever'])
            f.gift.claimed = True
            f.gift.save()
            f.save()
            return redirect('group_detail', slug=slug)

    context = {
        'group':group,
        'time_left':time_left,
        'gifts':gifts,
        'slug':slug,
        'show_add': True if days_left.days > 0 else False,
        'form':form,
        
    }

    return render(request, 'gift_registry/group_detail.html',context)

def add_gift(request, slug):
    if not get_referer(request):
        raise Http404
    group = Group.objects.get(slug=slug)
    form = AddGiftForm(request.POST or None)
    context = {
        'form':form,
        'group':group,
        'slug':slug,
    }
    if request.method == 'POST':
        if form.is_valid():

            f = form.save(commit=False)
            f.group = group
            f.save()
            
            return redirect('group_detail', slug=slug)
            
    return render(request, 'gift_registry/add_gift.html', context)

def view_claimed(request, slug):
    if not get_referer(request):
        raise Http404
    
    group = Group.objects.get(slug=slug)
    queryset = Gifter.objects.filter(group=group)
    form = ClaimedForm(request.POST or None)

    choices = [("-------", "-------")]
    for x in queryset.values():
        if (x['name'],x['name']) not in choices:
            choices.append((x['name'],x['name']))
    
    form.fields['name'].choices = choices
    gifters_exist = True if queryset.exists() else False

    context = {
        'slug':slug,
        'form': form,
        'gifters_exist': gifters_exist
    }
    
    if request.method == "POST":
        if form.is_valid():
            queryset = Gifter.objects.filter(group=group, name__exact=form.cleaned_data['name'])
            gifts = [x.gift for x in queryset]
            
            context = {
                'slug':slug,
                'form': form,
                'gifters_exist': gifters_exist,
                'gifts': gifts
            }
            return render(request, 'gift_registry/view_claimed.html', context)
            

    return render(request, 'gift_registry/view_claimed.html', context)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all().order_by('-pub_date')
    serializer_class = GroupSerializer

class GiftViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows gifts to be viewed or edited
    """
    queryset = Gift.objects.all().order_by('group')
    serializer_class = GiftSerializer

class GifterViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows gifters to be viewed or edited
    """
    queryset = Gifter.objects.all().order_by('group')
    serializer_class = GifterSerializer