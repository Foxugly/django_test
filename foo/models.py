from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

# Create your models here.
class Bar(models.Model):
	name=models.CharField(max_length=100, verbose_name=_("name"))

	def get_absolute_url(self):
		return reverse('foo:bar_change', kwargs={'pk': self.pk})

	def get_add_url(self):
		return  reverse('foo:bar_add')

	def get_detail_url(self):
		return reverse('foo:bar_detail', kwargs={'pk': self.pk})

	def get_delete_url(self):
		return reverse('foo:bar_delete', kwargs={'pk': self.pk})

	def get_list_url(self):
		return reverse('foo:bar_list')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _('Bar')


class Multibar(models.Model):
	name=models.CharField(max_length=100, verbose_name=_("name"))

	def get_absolute_url(self):
		return reverse('foo:multibar_change', kwargs={'pk': self.pk})

	def get_add_url(self):
		return  reverse('foo:multibar_add')

	def get_detail_url(self):
		return reverse('foo:multibar_detail', kwargs={'pk': self.pk})

	def get_delete_url(self):
		return reverse('foo:multibar_delete', kwargs={'pk': self.pk})

	def get_list_url(self):
		return reverse('foo:multibar_list')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _('Multibar')


class Foo(models.Model):
	name = models.CharField(max_length=100, verbose_name=_("name"))
	bar = models.ForeignKey(Bar, on_delete=models.CASCADE, verbose_name=_("bar"))
	multibars = models.ManyToManyField(Multibar, blank=True, verbose_name=_("multibars"))

	def get_absolute_url(self):
		return reverse('foo:foo_change', kwargs={'pk': self.pk})

	def get_add_url(self):
		return  reverse('foo:foo_add')

	def get_detail_url(self):
		return reverse('foo:foo_detail', kwargs={'pk': self.pk})

	def get_delete_url(self):
		return reverse('foo:foo_delete', kwargs={'pk': self.pk})

	def get_list_url(self):
		return reverse('foo:foo_list')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _('Foo')