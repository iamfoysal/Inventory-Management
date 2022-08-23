from django.urls import path

from . import views

# Shpo Routing

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', views.productlist, name='product-list'),
    path('api/add/', views.addproduct, name='product-add'),

<<<<<<< HEAD
    path('api/detail/<str:pk>/', views.detail, name='product-detail'),
    path('api/update/<str:pk>/', views.update, name='product-update'),
    path('api/delete/<str:pk>/', views.delete, name='product-delete'),
]
=======
    path('detail/<int:pk>/', views.product_detail, name='product-detail'),
    path('update/<int:id>/', views.product_update, name='product-update'),
    path('delete/<int:pk>/', views.product_delete, name='product-delete'),


    #genaral view
    path('home/', views.home, name='home'),
    path('add-prodcut/', views.add_product, name='add-product'),

]
>>>>>>> d6484a4f71962e19af781d88b6799687525155e6
