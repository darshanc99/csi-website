#Importing Dependencies
from django.conf.urls import url
from . import views

urlpatterns = [
    #/events/
    url(r'^$', views.index, name='events'),

    #/events/712/
    url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),
]