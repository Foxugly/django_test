from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from foo.models import Foo, Bar, Multibar
from django.urls import reverse_lazy
from view_breadcrumbs import ListBreadcrumbMixin, UpdateBreadcrumbMixin, DetailBreadcrumbMixin, CreateBreadcrumbMixin


class FooCreateView(CreateBreadcrumbMixin, CreateView):
    model = Foo
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('foo:foo_list')


class BarCreateView(CreateBreadcrumbMixin, CreateView):
    model = Bar
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('foo:bar_list')


class MultibarCreateView(CreateBreadcrumbMixin, CreateView):
    model = Multibar
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('foo:multibar_list')


class FooListView(ListBreadcrumbMixin, ListView):
    model = Foo
    paginate_by = 10
    ordering = ['pk']
    template_name = 'list.html'
    success_url = reverse_lazy('foo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class BarListView(ListBreadcrumbMixin, ListView):
    model = Bar
    paginate_by = 10
    ordering = ['pk']
    template_name = 'list.html'
    success_url = reverse_lazy('foo:bar_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class MultibarListView(ListBreadcrumbMixin, ListView):
    model = Multibar
    paginate_by = 10
    ordering = ['pk']
    template_name = 'list.html'
    success_url = reverse_lazy('foo:multibar_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class FooUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Foo
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('foo:foo_list')

    def get_object(self):
        return Foo.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class BarUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Bar
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('foo:bar_list')

    def get_object(self):
        return Bar.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class MultibarUpdateView(UpdateBreadcrumbMixin, UpdateView):
    model = Multibar
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('foo:multibar_list')

    def get_object(self):
        return Multibar.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        return context


class FooDetailView(DetailBreadcrumbMixin, DetailView):
    model = Foo
    template_name = 'detail.html'


class BarDetailView(DetailBreadcrumbMixin, DetailView):
    model = Bar
    template_name = 'detail.html'


class MultibarDetailView(DetailBreadcrumbMixin, DetailView):
    model = Multibar
    template_name = 'detail.html'


class FooDeleteView(DeleteView):
    model = Foo

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('foo:foo_list')


class BarDeleteView(DeleteView):
    model = Bar

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('foo:bar_list')


class MultibarDeleteView(DeleteView):
    model = Multibar

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('foo:multibar_list')
