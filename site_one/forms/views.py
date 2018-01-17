from django.shortcuts import render
from .forms import RegisterForm
from .models import RegisterForm as reg
from django.views.generic import TemplateView, ListView


# Create your views here.
def index(request):
	form = RegisterForm()
	context={
		"myregistrationform" : form
	}
	return render(request,"forms/index.html",context)

def second(request):

	context = {
		"fnm" : request.GET['firstname'],
		"lnm" : request.GET['lastname'],
		"email" : request.GET['email'],
		"password" : request.GET['password'],
	}
	p = reg()
	p.firstname = request.GET['firstname'],
	p.lastname = (request.GET['lastname']),
	p.email = request.GET['email'],
	p.password = request.GET['password'],
	p.save()
	return render(request,'forms/second.html',context)


def show(request):
	query_results = reg.objects.all()
	return render(request,'forms/show.html',{'query_results':query_results})

def delete(request):	
	if request.method == 'GET' and 'update' in request.GET:
		update = request.GET['update']

		if update is not None and update != '':
			reg.objects.filter(id=request.GET['update']
				).update(firstname=request.GET['firstname'])

	if request.method == 'GET' and 'delete' in request.GET:
		delete = request.GET['delete']

		if delete is not None and delete != '':
			'''query = reg.objects.get(id = request.GET['delete'])
			query.delete()'''
			reg.objects.get(id = request.GET['delete']).delete()

	

	

	return render(request,'forms/delete.html',{})


