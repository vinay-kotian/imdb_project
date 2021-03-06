"""imdb_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from imdb_app import views


urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^movies/$', views.movie_list),
    url(r'^movies/(?P<name>[0-9,a-z,A-Z]+)/$', views.movie_detail),
    url(r'^director/(?P<director_name>[0-9,a-z,A-Z]+)/$', views.directors_list),
    url(r'^genre_list/(?P<genre>[0-9,a-z,A-Z]+)/$', views.genre_list),
    url(r'^recomended_movies/(?P<movie_name>[0-9,a-z,A-Z]+)/$', views.recomended_movies),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
urlpatterns = format_suffix_patterns(urlpatterns)