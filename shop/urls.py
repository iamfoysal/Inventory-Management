from django.urls import path
from . import views

# Shpo Routing

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', views.productlist, name='product-list'),
    path('api/add/', views.addproduct, name='product-add'),

    path('api/detail/<str:pk>/', views.detail, name='product-detail'),
    path('api/update/<str:pk>/', views.update, name='product-update'),
    path('api/delete/<str:pk>/', views.delete, name='product-delete'),
]