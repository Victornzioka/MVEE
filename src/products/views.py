# from django.shortcuts import render

# from .models import Product
# from store.utils import cartData
# # Create your views here.
# def productsStore(request):
#     products = Product.objects.all()
	
# 	data = cartData(request)
# 	cartItems = data['cartItems']

# 	context = {'products':products, 'cartItems':cartItems}
# 	return render(request, 'store/store.html', context)

import json
import requests
from requests.auth import HTTPBasicAuth
from django.http import HttpResponse


def getAccessToken(request):
	consumer_key = 'bYTqy2EX0eZXmMnEAgRxeJYv19EDCF12'
	consumer_secret = 'mAWQfSQlqC28udgb'
	api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

	r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
	# print(r.text.encode('utf8'))
	mpesa_access_token = json.loads(r.text)
	validated_mpesa_access_token = mpesa_access_token['access_token']

	return HttpResponse(validated_mpesa_access_token)