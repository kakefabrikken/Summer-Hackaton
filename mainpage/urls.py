from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mainpage.views.index', name='index'),
    url(r'^blog/', include('blog.urls')),

)
