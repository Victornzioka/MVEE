from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import datetime
import json


from .models import *
from .utils import cartData

# Create your views here.
def store(request):
	products = Product.objects.all()
	
	data = cartData(request)
	cartItems = data['cartItems']

	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)

def cart(request):
	data = cartData(request)
	items = data['items']
	order = data['order']
	cartItems = data['cartItems']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)
	items = data['items']
	order = data['order']
	cartItems = data['cartItems'] 

	context = {'items':items, 'cartItems':cartItems, 'order':order}
	return render(request, 'store/checkout.html', context)

def DetailView(request, pk):
	detail = Product.objects.get(id=pk)

	data = cartData(request)
	cartItems = data['cartItems']

	context = {'detail':detail, 'cartItems':cartItems}
	return render(request, 'store/detail.html', context)

def updateItem(request):
	data = json.loads(request.body)
	action = data['action']
	productId = data['productId']

	print('productId:',productId)
	print('Action:', action)

	customer = request.user.customer
	product = Product.objects.get(id=productId)

	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	data = json.loads(request.body)
	transaction_id = datetime.datetime.now().timestamp()

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		total = float(data['CustomerData']['totals'])
		order.transaction_id = transaction_id

		if total == order.cart_totals:
			order.complete = True
		order.save()
		
	else:
		print('user is not logged in...')
	return JsonResponse('Payment complete...', safe=False)


def about(request):
	return render(request, 'store/about.html')

def home(request):
	return render(request, 'store/home.html')

#The view for the other products other than house plans
def store2(request):
	products = OtherProducts.objects.all()
	
	data = cartData(request)
	cartItems = data['cartItems']

	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/otherproducts.html', context)