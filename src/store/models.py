from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

# Create your models here.
class Customer(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=100)
	email = models.EmailField()

	def __str__(self):
		return self.name

@receiver(post_save, sender=User)
def assign_user_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_customer(sender, instance, **kwargs):
    instance.customer.save()

class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(decimal_places=2, max_digits=9)
	description = models.TextField(null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	
	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except Exception as e:
			url = ''
		return url
	

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(default=now)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=200)

	def __str__(self):
		return str(self.id)


	@property
	def cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

	@property
	def cart_totals(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total
	
	

class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
	quantity = models.IntegerField(default=0)
	date_added = models.DateTimeField(default=now)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total
	