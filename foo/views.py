from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from foo.models import Foo, Bar, Multibar
from django.urls import reverse_lazy


class FooCreateView(CreateView):
	model = Foo
	fields = ['name', 'bar', 'multibars']
	template_name = 'update.html'
	success_url = reverse_lazy('foo-list')


class BarCreateView(CreateView):
	model = Bar
	fields = ['name']
	template_name = 'update.html'
	success_url = reverse_lazy('bar-list')


class MultibarCreateView(CreateView):
	model = Multibar
	fields = ['name']
	template_name = 'update.html'
	success_url = reverse_lazy('multibar-list')


class FooListView(ListView):
	model = Foo
	paginate_by = 10
	template_name = 'list.html'
	success_url = reverse_lazy('foo-list')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


class BarListView(ListView):
	model = Bar
	paginate_by = 10
	template_name = 'list.html'
	success_url = reverse_lazy('bar-list')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


class MultibarListView(ListView):
	model = Multibar
	paginate_by = 10
	template_name = 'list.html'
	success_url = reverse_lazy('multibar-list')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context



class FooDetailView(DetailView):
	model = Foo
	fields = ['name', 'bar', 'multibars']
	template_name = 'detail.html'
	success_url = reverse_lazy('foo')

	def get_object(self):
		return Foo.objects.get(id=self.kwargs['id'])


class BarDetailView(DetailView):
	model = Bar
	fields = ['name']
	template_name = 'detail.html'
	success_url = reverse_lazy('bar')

	def get_object(self):
		return Bar.objects.get(id=self.kwargs['id'])


class MultibarDetailView(DetailView):
	model = Multibar
	fields = ['name']
	template_name = 'detail.html'
	success_url = reverse_lazy('multibar')

	def get_object(self):
		return Multibar.objects.get(id=self.kwargs['id'])




class FooUpdateView(UpdateView):
	model = Foo
	fields = ['name', 'bar', 'multibars']
	template_name = 'update.html'
	success_url = reverse_lazy('foo-list')

	def get_object(self):
		return Foo.objects.get(id=self.kwargs['id'])


class BarUpdateView(UpdateView):
	model = Bar
	fields = ['name']
	template_name = 'update.html'
	success_url = reverse_lazy('bar-list')

	def get_object(self):
		return Bar.objects.get(id=self.kwargs['id'])


class MultibarUpdateView(UpdateView):
	model = Multibar
	fields = ['name']
	template_name = 'update.html'
	success_url = reverse_lazy('multibar-list')

	def get_object(self):
		return Multibar.objects.get(id=self.kwargs['id'])