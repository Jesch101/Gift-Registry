from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name = 'home_view'),
    path('create_group/', views.create_group, name='create_group'),
    path('join_group/',views.join_group, name='join_group')
]