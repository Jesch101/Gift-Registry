from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from gift_registry import views

router = routers.DefaultRouter()
router.register(r'gifts', views.GiftViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'gifters', views.GifterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gift_registry.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
