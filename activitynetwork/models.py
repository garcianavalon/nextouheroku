from django.db import models
from django.contrib.auth.models import User

class Need(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class Activity(models.Model):
    act_holder = models.ForeignKey(User)
    name = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    datetime = models.DateTimeField('activity date')
    description = models.CharField(max_length=100)
    need = models.ManyToManyField(Need)
    category = models.ForeignKey(Category)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name

class Schedule(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    datetime = models.DateTimeField('schedule date')
    activity = models.ForeignKey(Activity)
    def __unicode__(self):
        return self.name
