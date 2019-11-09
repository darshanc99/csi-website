#Import Dependencies
from django.http import Http404
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	template = loader.get_template('homepage/homepage.html')
	context = {}
	return HttpResponse(template.render(context,request))