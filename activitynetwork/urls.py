from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from activitynetwork import views

urlpatterns = patterns('',
    url(r'^create/$',login_required(views.ActivityCreateView.as_view()), name='create'),
    url(r'^list/$',views.ActivityListView.as_view(), name='list'),
    url(r'^list/(?P<category>[\w\s]+)/$',views.ActivityListView.as_view(), name='filtered_list'),
    url(r'(?P<username>[\.\w-]+)/following/$',
        login_required(views.ActivityFollowingListView.as_view()), name='following'),
    url(r'(?P<username>[\.\w-]+)/hosting/$',
        login_required(views.ActivityHostingListView.as_view()), name='hosting'),
)