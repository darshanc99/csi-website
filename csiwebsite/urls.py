#Importing Dependencies
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    path('',include('homepage.urls'),name='home'), #Directs to the homepage!
    url(r'^admin/', admin.site.urls),
    url(r'^events/', include('event.urls')), #Directs to event app!
    url(r'^council/',include('members.urls')), #Directs to members app!
]