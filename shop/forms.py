from django.forms import ModelForm
from .models import Product, Category

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'stock', 'category', 'description', 'image']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

  


