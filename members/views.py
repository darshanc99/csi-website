
from django.http import Http404
from members.models import Batch
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	all_batch=Batch.objects.all()
	template=loader.get_template('members/index.html')
	context = {
	         'all_batch' : all_batch,
	          }
	return HttpResponse(template.render(context, request))

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
			
		
    except Batch.DoesNotExist:
        raise Http404("batch does not exist")
    return render(request,'members/members_detail.html',{'groups':groups})   