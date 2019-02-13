"""boot4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from foo.views import FooListView, BarListView, MultibarListView, FooUpdateView, BarUpdateView, MultibarUpdateView, FooCreateView, BarCreateView, MultibarCreateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path('foo/', FooListView.as_view(), name='foo-list'),
	path('bar/', BarListView.as_view(), name='bar-list'),
	path('multibar/', MultibarListView.as_view(), name='multibar-list'),

	path('foo/add/',FooCreateView.as_view(), name="foo-create"),
	path('bar/add/',BarCreateView.as_view(), name="bar-create"),
	path('multibar/add/',MultibarCreateView.as_view(), name="multibar-create"),

	path('foo/<int:id>/',FooUpdateView.as_view(), name="foo"),
	path('bar/<int:id>/',BarUpdateView.as_view(), name="bar"),
	path('multibar/<int:id>/',MultibarUpdateView.as_view(), name="multibar"),

    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
