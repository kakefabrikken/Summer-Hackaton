from django.conf.urls import patterns, url
#from blog import views

urlpatterns = patterns('',
        #url(r'^$', 'blog.views.blogindex', name='blog'),
        url(r'^$', 'blog.views.blogindex', name='blogindex'),
)
