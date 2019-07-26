from django.db import models
import datetime

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=120)
	articles = models.IntegerField()

	def __str__(self):
		return self.name

class Close(models.Model):
	name = models.CharField(max_length=50)
	date = models.DateField(blank=True, null=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.name
