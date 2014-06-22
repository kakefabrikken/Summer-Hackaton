from django.conf.urls import patterns, url

urlpatterns = patterns('', #<-- if all functions start with same 
        url(r'^$', 'blog.views.blogindex', name="blogindex"), # /blog
        url(r'^(?P<writer>[a-z]+)$', 'blog.views.writerpage'), #/blog/writer
        url(r'^(?P<writer>[a-z]+)/(?P<title_entered>[^/]+)', 'blog.views.blogpost'), #/blog/writer/title
)
