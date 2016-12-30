# -*- coding: UTF-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from heroku import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='django_index_view'),
    url(r'^admin/', include(admin.site.urls)),
]
urlpatterns += staticfiles_urlpatterns()
