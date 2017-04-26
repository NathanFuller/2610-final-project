from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Statement(models.Model):
	"""This is what I'm calling the forum posts"""
	author = models.CharField(max_length=32)
	content = models.TextField(max_length=1000)
	votes = models.IntegerField(default=0)
	date = models.DateTimeField('date of posting')
	def sortableDate(self):
		return self.date.strftime('%y%m%d%H%M%S')
	def __str__(self):
		if len(self.content)>32:
			return self.content[:32]+'...'
		else:
			return self.content

#note: s.date = datetime.datetime.now()