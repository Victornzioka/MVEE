from django.db import models

# Create your models here.
class HousePlan(models.Model):
	PlanName = models.CharField(max_length=120)
	PlanImage = models.ImageField()
	RegularPrice = models.DecimalField(max_digits=9, decimal_places=2)
	SalePrice = models.DecimalField(max_digits=9, decimal_places=2)
	PlanFile = models.FileField()

	def __str__(self):
		return self.PlanName

class HireArchitect(models.Model):
	PlanName = models.CharField(max_length=120)
	PlanDescription = models.TextField()
	TimeLimit = models.IntegerField()
	Payment = models.DecimalField(max_digits=9, decimal_places=2, null=True)

	def __str__(self):
		return self.PlanName