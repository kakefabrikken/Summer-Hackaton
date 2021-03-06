from django.db import models
from django.utils import timezone
# Create your models here.


class Writer(models.Model):
	firstname = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	email = models.EmailField(max_length=75)
	telephone = models.CharField(max_length=20)
	picture = models.ImageField(upload_to='media/images/')
	about = models.TextField()

	def __unicode__(self):
		return self.firstname


class Blogpost(models.Model):
	title = models.CharField(max_length=50)
	text = models.TextField()
	created_date = models.DateTimeField(auto_now=True)
	writers = models.ManyToManyField(Writer, through="Blogpost_writer")

	def __unicode__(self):
		return self.text

#	def was_published_recently(self, day_count):
#		if (day_count > 0):
#			return self.created_date >= timezone.now() - datetime.timedelta(days=day_count)
#		else:
#			return self.created_date >= timezone.now() - datetime.timedelta(days=1)
			


class Blogpost_writer(models.Model):
	writer = models.ForeignKey(Writer)
	blogpost= models.ForeignKey(Blogpost)
