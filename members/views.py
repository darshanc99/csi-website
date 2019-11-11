
from django.http import Http404
from members.models import Batch
from django.template import loader
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactForm
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client import service_account
import json
# Create your views here.
# def index(request):
# 	all_batch=Batch.objects.all()
# 	template=loader.get_template('members/index.html')
# 	context = {
# 	         'all_batch' : all_batch,
# 	          }
# 	return HttpResponse(template.render(context, request))


def contact_form(request):
    all_batch = Batch.objects.all()
    template = loader.get_template('members/index.html')
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
            return redirect("/council/")
        else:
            return HttpResponse("Fill the form!")

    form = ContactForm

    return render(
        request,'members/index.html',{
            "form":form,
            "all_batch":all_batch,
            }
    )



def detail(request, member_id):
    try:
        batch = Batch.objects.get(pk=member_id)
        q_set = batch.batchdetails_set.all()
        groups = {}
        for person in q_set:
            if person.position not in groups:
                groups[person.position] = []
            groups[person.position].append(person)
        print(groups)
		
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
                return redirect("/council/" + str(member_id))
            else:
                return HttpResponse("Fill the form!")

        form = ContactForm
	

    except Batch.DoesNotExist:
        raise Http404("batch does not exist")
    return render(request,'members/members_detail.html',{'groups':groups,'form':form})   