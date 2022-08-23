from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Product
from .forms import ProductAddForm
from .serializers import ProductSerializer



def index(request):

	return HttpResponse("Inventory Application initialization.")
	
def home(request):
    product = Product.objects.all()
    # if request.method == 'POST':
    #     search = request.POST.get('search-product')
    #     results = Product.objects.filter(Q(title__icontains=search) | Q(category__icontains=search))
    #     context =  { 
	# 		 'results': results,
	# 		 'search': search
	# 	}
    #     return render(request, 'shop/search.html', context)
    context = {'products': product }
    return render (request, "shop/index.html", context)


def add_product(request):
	form = ProductAddForm()
	context = {
		'form' : form
	}

	return render (request,'shop/add-product.html',context)

@api_view(['GET'])
def productlist(request):
	products = Product.objects.all().order_by('-created_at')
	product_serializer = ProductSerializer(products, many=True)
	return Response(product_serializer.data)

@api_view(['POST'])
def addproduct(request):
	products = ProductSerializer(data=request.data)
	if products.is_valid():
		products.save()
	return Response(products.data)

@api_view(['POST'])
def update(request, pk):
	product = Product.objects.get(id=pk)
	product_serializer = ProductSerializer(instance=product, data=request.data)
	if product_serializer.is_valid():
		product_serializer.save()
	return Response(product_serializer.data)

@api_view(['GET'])
def detail(request, pk):
	product = Product.objects.get(id=pk)
	product_serializer = ProductSerializer(product, many=False)
	return Response(product_serializer.data)


@api_view(['DELETE'])
def delete(request, pk):
	product = Product.objects.get(id=pk)
	product.delete()
	return Response("Product deleted")

