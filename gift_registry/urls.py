from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name = 'home_view'),
    path('create-group/', views.create_group, name='create_group'),
    path('view-group/',views.find_group, name='view_group'),
    path('view-group/<slug:slug>/', views.group_detail, name='group_detail'),
    path('view-group/<slug:slug>/add-gift/', views.add_gift, name='add_gift'),
    path('view-group/<slug:slug>/view-claimed/',views.view_claimed, name='view_claimed')
]