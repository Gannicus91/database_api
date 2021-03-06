"""database_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from university import views
from django.views.generic import RedirectView

urlpatterns = [
    #    path('admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url="teachers/", permanent=True), name='index'),
    url(r'^teachers/$', views.teachers, name='teachers'),
    url(r'^subjects/$', views.subjects, name='subjects'),
    url(r'^academic_plan/$', views.academic_plan, name='academic_plan'),
    url(r'^groups/$', views.groups, name='groups'),
    url(r'^lessons/$', views.lessons, name='lessons'),
    url(r'^login/$', views.login, name='login'),

    url(r'^(?P<table>\w+)/add/$', views.add_entity_page, name='add-entity'),
    url(r'^(?P<table>\w+)/edit/(?P<item_id>\d+)/$', views.edit_entity_page, name='edit-entity'),

    url(r'^api/v1/(?P<table>\w+)/$', views.add_entity, name='api-add-entity'),
    url(r'^api/v1/(?P<table>\w+)/(?P<item_id>\d+)/$', views.edit_delete_entity, name='api-entity'),
]
