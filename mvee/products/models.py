from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(decimal_places=2, max_digits=9)
	description = models.TextField(null=True, blank=True)
	featured = models.ImageField(null=True, blank=True)
	
	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.featured.url
		except Exception as e:
			url = ''
		return url