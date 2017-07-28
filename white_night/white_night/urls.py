"""white_night URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url , include
from django.contrib import admin
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^item/', include('list_item_info.urls'))
 
]
from django.conf import settings
# from django.contrib.staticfiles import views

# if settings.DEBUG:
#     urlpatterns += [
#         url(r'^static/(?P<path>.*)$', views.serve),
#     ]




# Build paths inside the project like this: os.path.join(BASE_DIR, ...)