#Import Dependencies
from django.http import Http404
from .models import Event
from django.template import loader
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactForm
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client import service_account
import json


def contact_form(request):
    all_events = Event.objects.all()
    template = loader.get_template('event/index.html')
    if request.method =='POST':
        DIRNAME = os.path.dirname(__file__)
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
            credentials = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(DIRNAME,'credential.json'), scope)
            gs = gspread.authorize(credentials)
            wsheet = gs.open_by_url("https://docs.google.com/spreadsheets/d/1n3vAb3NeW-C1kr0_vgwiuSNCoQ3uc0jGyTBUjRozMmY/edit?usp=sharing").sheet1
            wsheet.append_row([name,email,message])
            return redirect("/events/")
        else:
            return HttpResponse("Fill the form!")

    form = ContactForm

    return render(
        request,'event/index.html',{
            "form":form,
            "all_events":all_events,
            }
    )


# def index(request):
#     all_events = Event.objects.all()
#     template = loader.get_template('event/index.html')
#     context = {
#         'all_events' : all_events,
#     }
#     return HttpResponse(template.render(context, request))

def detail(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
        template = 'event/event_detail.html'
        #context = {'event':event}
        form = ContactForm

        if request.method =='POST':
            DIRNAME = os.path.dirname(__file__)
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data.get('name')
                email = form.cleaned_data.get('email')
                message = form.cleaned_data.get('message')
                scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
                credentials = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(DIRNAME,'credential.json'),scope)
                gs = gspread.authorize(credentials)
                wsheet = gs.open_by_url("https://docs.google.com/spreadsheets/d/1n3vAb3NeW-C1kr0_vgwiuSNCoQ3uc0jGyTBUjRozMmY/edit?usp=sharing").sheet1
                wsheet.append_row([name,email,message])
                return redirect("/events/" + str(event_id))
            else:
                return HttpResponse("Fill the form!")

        form = ContactForm


    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    return render(request,template,{'event':event,'form':form})
    # return HttpResponse(template.render(context,request))