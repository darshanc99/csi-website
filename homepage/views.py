#Import Dependencies
from django.http import Http404
from django.template import loader
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactForm
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client import service_account
import json
import os

def contact_form(request):
	template = loader.get_template('homepage/homepage.html')
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
			return redirect("/")
		else:
			return HttpResponse("Fill the form!")

	form = ContactForm

	return render(
		request,'homepage/homepage.html',{"form":form}
	)
