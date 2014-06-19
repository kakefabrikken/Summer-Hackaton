from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.

from blog.models import Writer
from blog.models import Blogpost

admin.site.register(Writer)
admin.site.register(Blogpost, MarkdownModelAdmin)
