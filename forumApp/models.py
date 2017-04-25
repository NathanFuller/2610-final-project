from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Statement(models.Model):
	author = models.CharField(max_length=32)
	content = models.TextField(max_length=1000)
	votes = models.IntegerField(default=0)
	date = models.DateTimeField('date published')

