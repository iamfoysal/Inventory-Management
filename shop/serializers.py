from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'stock', 'category', 'description', 'image')


    # Delete the old image from the folder when the product is updated   
    # def save(self, *args, **kwargs):
    #     if self.instance.image:
    #         self.instance.image.delete()
    #     return super().save(*args, **kwargs)