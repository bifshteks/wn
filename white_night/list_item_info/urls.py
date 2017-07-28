from django.conf.urls import url
from list_item_info.views import PostsListView, PostDetailView, mail
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))








urlpatterns = [
	url(r'^$', PostsListView.as_view(), name='list'),

	url(r'^(?P<pk>\d+)/$', PostDetailView.iteminfo_detail, name='iteminfo_detail'),

	]