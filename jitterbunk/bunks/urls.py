from django.conf.urls import url
# from django.urls import path, include

from . import views

app_name = 'bunks'
urlpatterns = [
    # ex: /bunks/
    url(r'^$', views.index, name='index'),
    # ex: /bunks/5/
    url(r'^(?P<user_id>[0-9]+)/$', views.main, name='main'),
    # ex: /bunks/5/bunk/
    url(r'^(?P<user_id>[0-9]+)/bunk/$', views.bunk, name='bunk'),
]
