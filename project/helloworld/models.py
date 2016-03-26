from __future__ import unicode_literals

from django.db import models

# Create your models here

class Priority(models.Model):
	value  = models.IntegerField(default=0)
	
	class Meta:
		verbose_name_plural = "Priorities"

	def __unicode__(self):
		return unicode(self.value)

class Job(models.Model):
	name = models.CharField(max_length=20, unique=True)
	description = models.CharField(max_length=100)
	date = models.DateField()
	priority = models.ForeignKey(Priority)

	class Meta:
		verbose_name_plural = "Jobs"

	def __unicode__(self):
		return self.name
