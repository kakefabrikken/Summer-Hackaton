from django.db import models
from django_markdown.widgets import Markdownwidget

class PictureForm(forms.Form):
    picture = forms.ImageField()

class MycustomForm(forms.Form):
    content = forms.CharField(widget=MarkdownWidget())

