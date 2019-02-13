from django.db import models
from django.urls import reverse


# Create your models here.
class Bar(models.Model):
	name=models.CharField(max_length=100)

	def get_absolute_url(self):
		return reverse('bar', kwargs={'id': self.pk})

	def add_url(self):
		return  reverse('bar-add')

	def url(self):
		return reverse('bar-list')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Bar'


class Multibar(models.Model):
	name=models.CharField(max_length=100)

	def get_absolute_url(self):
		return reverse('multibar', kwargs={'id': self.pk})

	def add_url(self):
		return reverse('multibar-add')

	def url(self):
		return reverse('multibar-list')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Multibar'


class Foo(models.Model):
	name = models.CharField(max_length=100)
	bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
	multibars = models.ManyToManyField(Multibar, blank=True)

	def get_absolute_url(self):
		return reverse('foo', kwargs={'id': self.pk})

	def add_url(self):
		return  reverse('foo-add')

	def url(self):
		return reverse('foo-list')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Foo'