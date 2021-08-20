from django.urls import path

from .import views

urlpatterns = [
	path('',views.home, name='home'),
	path('store/',views.store, name='store'),
	path('cart/',views.cart, name='cart'),
	path('detail/<int:pk>/',views.DetailView, name='detail'),
	path('update_item/', views.updateItem, name='update_item'),
	path('checkout/', views.checkout, name='checkout'),
	path('process_order/', views.processOrder, name='process_order'),
	path('about/', views.about, name='about'),
	path('products/', views.store2, name='other_products'),
]