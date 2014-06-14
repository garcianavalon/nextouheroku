from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from activitynetwork.models import Activity, Category
from activitynetwork.forms import ActivityForm
from django.shortcuts import redirect

class ActivityCreateView(CreateView):
    model = Activity
    form_class = ActivityForm
    #fields = ['name']
    success_url = '/activities/list/'
    template_name = "activity_create.html"

    def form_valid(self, form):
        object = form.save(commit=False)
        object.act_holder = self.request.user
        object.save()
        return super(ActivityCreateView, self).form_valid(form)

class ActivityListView(ListView):
    model = Activity
    template_name = "activity_list.html"
    def get_context_data(self, **kwargs):
        context = super(ActivityListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        user = self.request.user
        if user.is_authenticated():
            f_activities = []
            followed_activities = Activity.objects.filter(followed_activites__id=user.volunteer_profile.id)
            for f_activity in followed_activities:
                f_activities.append(f_activity.id)
            context['f_activities'] = f_activities
        return context
    def get_queryset(self):
        category = self.kwargs.get('category','All')#default value
        if not category or category == 'All':
            return Activity.objects.all()
        else:
            category_object = Category.objects.get(name=category)
            return Activity.objects.filter(category=category_object)

    def post(self, request, *args, **kwargs):
        act_id = request.POST['activity_id']
        activity = Activity.objects.get(id=act_id)
        user = request.user
        if user.is_authenticated():
            profile = user.volunteer_profile
            if activity in Activity.objects.filter(followed_activites__id=profile.id):
                profile.followed_activites.remove(activity)
            else:
                profile.followed_activites.add(activity)
        return redirect('activities:list') # Redirect after POST


class ActivityFollowingListView(ListView):
    model = Activity
    template_name = "activity_following_list.html"
    def get_context_data(self, **kwargs):
        context = super(ActivityFollowingListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated():
            context['activity_list'] = Activity.objects.filter(followed_activites__id=user.volunteer_profile.id)
        return context
    def post(self, request, *args, **kwargs):
        act_id = request.POST['activity_id']
        activity = Activity.objects.get(id=act_id)
        user = request.user
        if user.is_authenticated():
            profile = user.volunteer_profile
            if activity in Activity.objects.filter(followed_activites__id=profile.id):
                profile.followed_activites.remove(activity)
            else:
                profile.followed_activites.add(activity)
        return redirect('activities:following',username=user.username) # Redirect after POST

class ActivityHostingListView(ListView):
    model = Activity
    template_name = "activity_hosting_list.html"
    def get_context_data(self, **kwargs):
        context = super(ActivityHostingListView, self).get_context_data(**kwargs)
        user_name = self.kwargs['username']
        context['user'] = User.objects.get(username=user_name)
        context['activity_list'] = Activity.objects.filter(act_holder=context['user'].id)
        return context
