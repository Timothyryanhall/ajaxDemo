from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^clear$', views.clear),
    url(r'^all.json$', views.all_json),
    url(r'^all.html$', views.all_html),
    url(r'^find$', views.find),
    url(r'^create$', views.create),
    url(r'^findLastName$', views.findLastName),
    url(r'^monthFilter$', views.monthFilter),
    url(r'^lastNameOrder$', views.lastNameOrder),
    url(r'^firstToRegister$', views.firstToRegister),
    url(r'^dateRange$', views.dateRange),


]