#Importing Dependencies
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #/
    #path("",views.index,name='homepage')
    #url(r'^$', views.index, name='homepage'),
    #url(r'')
    url(r'^$', views.contact_form,name='homepage')
]