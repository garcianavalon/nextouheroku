from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from activitynetwork.models import Activity

class Talent(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self): # __unicode__ on Python 2
        return self.name

class VolunteerProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='volunteer_profile')

    name = models.CharField(_('name'),
                                max_length=20)
    followed_activites = models.ManyToManyField(Activity,related_name = 'followed_activites')

    intro = models.CharField(_('intro'),
                                max_length=140)
    resume = models.CharField(_('resume'),
                                max_length=1000)
    talents = models.ManyToManyField(Talent,related_name = 'talents'),

    participated_activities = models.ManyToManyField(Activity,related_name = 'participated_activities')

class Comment(models.Model):
	text = models.CharField(max_length=100)
	author = models.ForeignKey(User, related_name = 'Comment_author')
	receiver = models.ForeignKey(User, related_name = 'Comment_receiver') #the one who is reviewed

