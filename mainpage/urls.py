from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
#flatpages.register()

urlpatterns = patterns('',
    url(r'^$', 'mainpage.views.index', name='index'),
    url(r'^blog/', include('blog.urls')),
    url('^markdown/' , include( 'django_markdown.urls')),
    url(r'^admin/' , include(admin.site.urls)), 
)
