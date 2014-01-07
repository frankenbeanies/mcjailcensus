from django.db import models

class Inmate(models.Model):
	last = models.CharField(max_length=100)
	dob = models.DateField()
	sex = models.CharField(max_length=1)
	middle = models.CharField(max_length=1)
	race = models.CharField(max_length=1)
	mcid = models.IntegerField(max_length=6)
	first = models.CharField(max_length=100)