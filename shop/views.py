from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from django.db.models import Q
from .models import Product, Category



def index(request):

	return HttpResponse("Inventory Application initialization.")
	
# def index(request):
#     product = Product.objects.all()
#     if request.method == 'POST':
#         search = request.POST.get('search-product')
#         results = Product.objects.filter(Q(title__icontains=search) | Q(category__icontains=search))
#         context =  { 
# 			 'results': results,
# 			 'search': search
# 			 }
#         return render(request, 'shop/search.html', context)
  
#     context = {'product': product }
#     return render (request, "shop/index.html", context)


def product_detail(request, id):
	product = get_object_or_404(Product, pk=id)
	context = {'product': product}
	return render (request, "shop/product_detail.html", context)



@login_required
def product_update(request, pk):
	product = get_object_or_404(Product, pk=pk)
	if request.method == 'POST':
		product.title = request.POST.get('title')
		product.price = request.POST.get('price')
		product.stock = request.POST.get('stock')
		product.description = request.POST.get('description')
		product.save()
		return redirect('index')
	context = {'product': product}
	return render (request, "shop/product_update.html", context)



@login_required
def product_delete(request, id):
	product = get_object_or_404(Product, pk=id)
	product.delete()
	return redirect('index')



#api sections 

@api_view(['GET'])
def productlist(request):
	products = Product.objects.all().order_by('-created_at')
	serializer = ProductSerializer(products, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def addproduct(request):
	serializer = ProductSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)