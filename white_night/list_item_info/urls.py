from django.conf.urls import url
from list_item_info.views import PostsListView, PostDetailView 
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))








urlpatterns = [
	url(r'^$', PostsListView.as_view(), name='list'), # то есть по URL http://имя_сайта/blog/ 
                                               # будет выводиться список постов
	url(r'^(?P<pk>\d+)/$', PostDetailView.iteminfo_detail, name='iteminfo_detail',) # а по URL http://имя_сайта/blog/число/ 
                                              # будет выводиться пост с определенным номером
	]