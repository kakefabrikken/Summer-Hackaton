from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views', #<-- if all functions start with same 
        url(r'^$', blogindex, name='blogindex'), # /blog
        url(r'^(?P<writer>[a-z]+)$', writerpage), #/blog/writer
        url(r'^(?P<writer>[a-z]+)/(?P<title_entered>[^/]+)', blogpost), #/blog/writer/title
)
