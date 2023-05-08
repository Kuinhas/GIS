"""GIST URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from mygis import views

urlpatterns = [
    re_path('^$', views.home, name='home'),
    re_path(r'^about/', views.about, name='about'),
    re_path(r'^mymap/', views.mymap, name='mymap'),
    re_path(r'^articles/(?P<article_id>[0-9]+)/$', views.show_articles, name='article'),
]

# from django.contrib import admin
# from django.conf.urls import url

'''
urlpatterns = [
    url(r'^$', views.home, name='home'),
]
'''
