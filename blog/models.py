from django.db import models
from django.utils import timezone

class Writer(models.Model):
	firstname = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	email = models.EmailField(max_length=75)
	telephone = models.CharField(max_length=20)
	picture = models.ImageField(upload_to='media/images/')
	about = models.TextField()
        blogposts = models.ManyToManyField('Blogpost', through='Blogpost_writer')

	def __unicode__(self):
		return self.firstname

        class Meta:
            ordering = ('id',)


class Blogpost(models.Model):
	title = models.CharField(max_length=50)
	text = models.TextField()
	created_date = models.DateTimeField(auto_now=True)
	writers = models.ManyToManyField('Writer', through='Blogpost_writer')

	def __unicode__(self):
		return self.title

        class Meta:
            ordering = ('created_date',)

#	def was_published_recently(self, day_count):
#		if (day_count > 0):
#			return self.created_date >= timezone.now() - datetime.timedelta(days=day_count)
#		else:
#			return self.created_date >= timezone.now() - datetime.timedelta(days=1)


class Blogpost_writer(models.Model):
	writer = models.ForeignKey(Writer)
	blogpost= models.ForeignKey(Blogpost)

        class Meta:
            ordering = ('id',)

	def __unicode__(self):
            return str(self.id).decode('UTF-8') #convert int to unicode string
