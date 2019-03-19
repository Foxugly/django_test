from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from view_breadcrumbs import ListBreadcrumbMixin, UpdateBreadcrumbMixin, DetailBreadcrumbMixin, CreateBreadcrumbMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _


class GenericCreateView(SuccessMessageMixin, CreateBreadcrumbMixin, CreateView):
	model = None
	fields = '__all__'
    template_name = 'update.html'
    success_url = None
    success_message = _('object created.')
	
	def __init__(self, model, appname, classname):
		self.model = model
		self.success_url = reverse_lazy('%s:%s_list' % (appname, classname)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GenericListView(ListBreadcrumbMixin, ListView):
    model = None
    paginate_by = 10
    ordering = ['pk']
    template_name = 'list.html'

	def __init__(self, model):
		self.model = model
		
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class GenericUpdateView(SuccessMessageMixin, UpdateBreadcrumbMixin, UpdateView):
    model = None
    fields = '__all__'
    template_name = 'update.html'
    success_url = None
    success_message = _('object updated.')
	
	def __init__(self, model, appname, classname):
		self.model = model
		self.success_url = reverse_lazy('%s:%s_list' % (appname, classname)
		
    def get_object(self):
        return self.model.objects.get(pk=self.kwargs['pk'])
		# return get_object_or_404(self.model, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class GenericDetailView(DetailBreadcrumbMixin, DetailView):
    model = None
    template_name = 'detail.html'

	def __init__(self, model):
		self.model = model


class GenericDeleteView(SuccessMessageMixin, DeleteView):
    model = None
    success_message = _('object deleted.')

	def __init__(self, model, appname, classname):
		self.model = model
		self.success_url = reverse_lazy('%s:%s_list' % (appname, classname)
		
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return self.success_url
