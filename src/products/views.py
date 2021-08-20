from django.shortcuts import render

from .models import Product
from store.utils import cartData
# Create your views here.
def productsStore(request):
    products = Product.objects.all()
	
	data = cartData(request)
	cartItems = data['cartItems']

	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)