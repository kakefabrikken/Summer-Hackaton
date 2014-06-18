from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.

admin.site.register(Mymodel, MarkdownModelAdmin)
