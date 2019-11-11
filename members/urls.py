from django.conf.urls import url
from . import views

urlpatterns = [
    #/council/
    url(r'^$', views.contact_form, name='members'),

    #/council/712/
    url(r'^(?P<member_id>[0-9]+)/$', views.detail, name='detail'),
]