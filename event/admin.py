#Import Dependencies
from django.contrib import admin
from .models import Event, EventDetail

# Register your models here.
admin.site.register(Event)
admin.site.register(EventDetail)