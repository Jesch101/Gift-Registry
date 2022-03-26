from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name = 'home_view'),
    path('create-group/', views.create_group, name='create_group'),
    path('create-group/success',TemplateView.as_view(
        template_name='gift_registry/create_group_success.html'),
        name='group_success'),
    path('view-group/',views.view_group, name='view_group'),
    path('view-group/<slug:slug>/', views.group_detail, name='group_detail')
]