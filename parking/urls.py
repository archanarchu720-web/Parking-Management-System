
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/parking', views.ParkingViewSet)

urlpatterns = [
    # CRUD Pages
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),

    # API
    path('', include(router.urls)),
]