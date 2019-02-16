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
from django.urls import path, include
from foo.views import FooListView, BarListView, MultibarListView, FooUpdateView, BarUpdateView, MultibarUpdateView, FooCreateView, BarCreateView, MultibarCreateView
from django.conf.urls.static import static
from django.conf import settings
from django.apps import apps
from django.shortcuts import render


def home(request):
    c = {}
    available_apps = {}
    for app in apps.get_models():
        if not app.__module__.startswith("django"):
            a = app.__module__.split('.models')[0]
            if a in available_apps:
               available_apps[a].append(app)
            else:
                available_apps[a] = [app]
    c['apps'] = available_apps
    return render(request, "index.html", c)


def test(request):
    return render(request,"test.html")



urlpatterns = [

    path('', home, name='home'),
	path('foo/', FooListView.as_view(), name='foo-list'),
	path('bar/', BarListView.as_view(), name='bar-list'),
	path('multibar/', MultibarListView.as_view(), name='multibar-list'),
    path('test/', test, name='test'),
	path('foo/add/',FooCreateView.as_view(), name="foo-add"),
	path('bar/add/',BarCreateView.as_view(), name="bar-add"),
	path('multibar/add/',MultibarCreateView.as_view(), name="multibar-add"),

	path('foo/<int:id>/',FooUpdateView.as_view(), name="foo"),
	path('bar/<int:id>/',BarUpdateView.as_view(), name="bar"),
	path('multibar/<int:id>/',MultibarUpdateView.as_view(), name="multibar"),

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('hijack/', include('hijack.urls', namespace='hijack')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))]

