from django.db import models

class PictureForm(forms.Form):
    picture = forms.ImageField()
