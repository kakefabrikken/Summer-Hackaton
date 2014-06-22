from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import loader, Context
import re
from blog.models import Writer, Blogpost, Blogpost_writer

class Blogpostinfo:
    def __init__(self, title, slug, summary ):
        self.title = title
        self.slug  = slug
        self.summary = summary

def blogindex(request):
    #return render(request, 'blog/index.html')
    template = loader.get_template("blog/blog.html")
    c = Context({})
    return HttpResponse( template.render(c) )

def writerpage(request, writer):
    writer_number = getWriterID( writer )
    if (not writer_number):
        raise Http404()
    # get stuff from database
    writerObject = Writer.objects.get( id=writer_number )
    posts = writerObject.blogpost_set.all()
    postlist = []
    for post in posts:
        # title() changes strings to start each word with uppercase character
        title = post.title.title()
        slug = writer.title() + "/" + post.title.replace(' ', '_')
        summary = firstThreeSentences( post.text )
        postlist.append( Blogpostinfo( title,slug,summary ) )

    template = loader.get_template("blog/writer.html")
    c = Context({ 'writer': writer.title(), 'blogposts': postlist })
    return HttpResponse( template.render(c) )

def blogpost(request, writer, title_entered):
    db_title = title_entered.replace('_', ' ')
    writer_number = getWriterID( writer )
    if (not writer_number):
        raise Http404()
    # should check who wrote the blogpost here
    # should do something to include all writers in writerstring
    writerstring = writer
    blogpost = Blogpost.objects.get( title=db_title )
    if (not blogpost):
        raise Http404()

    template = loader.get_template("blog/blogpost.html")
    c = Context({ 'blogtitle':blogpost.title, 'text':blogpost.text, 'writers':writerstring  })
    return HttpResponse( template.render(c) )

def getWriterID( name ):
    name = name.lower()
    return {
# these numbers should be updated to match whatever the
# writer_id's are in the database
        'finn'    : 2,
        'kristian': 4,
        'marius'  : 3,
        'ilse'    : 1,
        'tobias'  : 5,
    }.get(name, 0)

def firstThreeSentences( blogpost ):
    last_char =[ m.start() for m in re.finditer( r"\. ",blogpost ) ][2]
    return blogpost[:last_char+1]

