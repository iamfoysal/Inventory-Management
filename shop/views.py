from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .forms import ProductAddForm
from .models import Category, Product
from django.contrib import messages



@login_required(login_url='/signin')
def index(request):
    product = Product.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search-product')
        results = Product.objects.filter(Q(title__icontains=search))
        context =  { 
			 'results': results,
			 'search': search
		}
        return render(request, 'shop/search.html', context)
    context = {'products': product }
    return render (request, "shop/index.html", context)


@login_required(login_url='/signin')
def add_product(request):
	if request.method == 'POST':
		form = ProductAddForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			print(form)
			messages.success(request, 'Product added successfully')
			return redirect('index')
	else:
		form = ProductAddForm()
	context = {'form': form}

	return render(request, 'shop/add-product.html', context)

'''
@login_required(login_url='/signin')
def delete_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/')

    context ={'product': product}
    return render (request, 'shop/delete.html', context)

'''
@api_view(['GET'])
def productlist_api(request):
	products = Product.objects.all().order_by('-created_at')
	# print(products)
	product_serializer = ProductSerializer(products, many=True)
	# print(product_serializer.data)
	return Response(product_serializer.data)



@api_view(['POST'])
def add_product_api(request):
	products = ProductSerializer(data=request.data)
	if products.is_valid():
		products.save()
	return Response(products.data)


@api_view(['POST'])
def update_product_api(request, pk):
	product = Product.objects.get(id=pk)
	product_serializer = ProductSerializer(instance=product, data=request.data)
	if product_serializer.is_valid():
		product_serializer.save()
	return Response(product_serializer.data)


@api_view(['GET'])
def detail_product_api(request, pk):
	product = Product.objects.get(id=pk)
	product_serializer = ProductSerializer(product, many=False)
	return Response(product_serializer.data)



@api_view(['DELETE'])
def delete_product_api(request, pk):
	product = Product.objects.get(id=pk)
	product.delete()
	return Response("Product deleted")

