#Import Dependencies
from django.http import Http404
from .models import Event
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    all_events = Event.objects.all()
    template = loader.get_template('event/index.html')
    context = {
        'all_events' : all_events,
    }
    return HttpResponse(template.render(context, request))

def detail(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
        template=loader.get_template('event/event_detail.html')
        context = { 'event':event, }
    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    return HttpResponse(template.render(context,request))