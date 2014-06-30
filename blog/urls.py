from django.conf.urls import patterns, url

urlpatterns = patterns('', #<-- if all functions start with same 
    # blog
    url(r'^$', 'blog.views.blogindex', name="blogindex"),

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
        
    # blog/writer - the first character can be uppercase
    url(r'^(?P<writer>[A-Za-z][a-z]+)$', 'blog.views.writerpage'),

    # blog/writer/title
    url(r'^(?P<writer>[A-Za-z][a-z]+)/(?P<title_entered>[^/]+)', 'blog.views.blogpost'),
)
