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
	time = datetime.datetime.now()
	value = models.IntegerField()

	def __str__(self):
		return self.name
