from foo.views import FooListView, BarListView, MultibarListView, FooUpdateView, BarUpdateView, MultibarUpdateView, FooDetailView, BarDetailView, MultibarDetailView, FooCreateView, BarCreateView, MultibarCreateView, FooDeleteView, BarDeleteView, MultibarDeleteView
from django.urls import path


app_name = 'foo'
urlpatterns = [
    path('foo/', FooListView.as_view(), name='foo_list'),
    path('bar/', BarListView.as_view(), name='bar_list'),
    path('multibar/', MultibarListView.as_view(), name='multibar_list'),
    path('foo/add/', FooCreateView.as_view(), name="foo_add"),
    path('bar/add/', BarCreateView.as_view(), name="bar_add"),
    path('multibar/add/', MultibarCreateView.as_view(), name="multibar_add"),
    path('foo/<int:pk>/change/', FooUpdateView.as_view(), name="foo_change"),
    path('bar/<int:pk>/change/', BarUpdateView.as_view(), name="bar_change"),
    path('multibar/<int:pk>/change/', MultibarUpdateView.as_view(), name="multibar_change"),
    path('foo/<int:pk>/', FooDetailView.as_view(), name="foo_detail"),
    path('bar/<int:pk>/', BarDetailView.as_view(), name="bar_detail"),
    path('multibar/<int:pk>/', MultibarDetailView.as_view(), name="multibar_detail"),
    path('foo/<int:pk>/delete', FooDeleteView.as_view(), name="foo_delete"),
    path('bar/<int:pk>/delete', BarDeleteView.as_view(), name="bar_delete"),
    path('multibar/<int:pk>/delete', MultibarDeleteView.as_view(), name="multibar_delete"),
]
