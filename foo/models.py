from django.db import models
from django.urls import reverse


# Create your models here.
class Bar(models.Model):
	name=models.CharField(max_length=100)

	def get_absolute_url(self):
		return reverse('bar', kwargs={'id': self.pk})

	def __str__(self):
		return self.name


class Multibar(models.Model):
	name=models.CharField(max_length=100)

	def get_absolute_url(self):
		return reverse('multibar', kwargs={'id': self.pk})

	def __str__(self):
		return self.name


class Foo(models.Model):
	name = models.CharField(max_length=100)
	bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
	multibars = models.ManyToManyField(Multibar, blank=True)

	def get_absolute_url(self):
		return reverse('foo', kwargs={'id': self.pk})

	def __str__(self):
		return self.name