from . models import *


def cartData(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order,created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.cart_items
	else:
		items = []
		order = {'cart_items':0, 'cart_totals':0}
		cartItems = order['cart_items']
	return {'items':items,'order':order, 'cartItems':cartItems}