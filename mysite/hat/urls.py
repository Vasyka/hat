from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rooms/$', views.rooms, name='rooms'),
    url(r'^rooms/(?P<room_id>[0-9]+)/$', views.room, name='room'),
    url(r'^profile/(?P<userprofile_id>[0-9]+)$', views.profile, name='profile'),
    url(r'^rating/$', views.rating, name='rating'),
    url(r'^rules/$', views.rules, name='rules'),
]
