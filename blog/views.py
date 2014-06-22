from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import loader, Context
import re

# Create your views here.
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
    postIDs = Blogpost_writer.objects.filter(writer_id == writer_number)
    posts = []
    postinfo= [][]
    for ID in postIDs:
        posts.append( Blogpost.objects.get(ID) )
    for post in posts:
        title = post.title
        summary = firstThreeSentences( post.text )
        postinfo.append( [title, summary] )

    template = loader.get_template("blog/writer.html")
    c = Context({ writer: writer, blogposts: postinfo })
    return HttpResponse( template.render(c) )

def blogpost(request, writer, title_entered):
    title = title_entered.replace('_', ' ')
    writer_number = getWriterID( writer )

def getWriterID( number ):
    return {
# these numbers should be updated to match whatever the
# writer_id's are in the database
        'finn'    : 2,
        'kristian': 4,
        'marius'  : 3,
        'ilse'    : 1,
        'tobias'  : 5,
    }.get(offset, 0)

def firstThreeSentences( blogpost ):
    last_char =[ m.start() for m in re.finditer( r". ",post.text ) ][2]
    return pos.text[:last_char]

