from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

# Create your views here.
def blogindex(request):
        print "rendering blog"
	#return render(request, 'blog/index.html')
        template = loader.get_template("blog/blog.html")
        c = Context({})
        return HttpResponse( template.render(c) )
