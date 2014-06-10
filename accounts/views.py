from django.shortcuts import render
from userena.views import ProfileListView
from accounts.models import Talent
# Create your views here.
class CustomProfileListView (ProfileListView):
    def get_context_data(self, **kwargs):
		context = super(CustomProfileListView, self).get_context_data(**kwargs)
		context['talents_list'] = Talent.objects.all()
		return context