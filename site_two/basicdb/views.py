from django.shortcuts import render
from . import models

# Create your views here.
def create(request):
	file = 'create_sec.html'
	if request.method == 'GET' and 'update' in request.GET:
		update(request)
		file = 'update.html'
	return render(request,file)

def update(request):
	#tbl_id = models.Register.objects.get(id = )
	obj = models.Register.objects.get(id=request.GET['id'])
	obj.name = request.GET['name']
	obj.state = request.GET['state']
	obj.city = request.GET['city']
	obj.contact = request.GET['contact']
	obj.password = request.GET['password']
	obj.save()

def save(request):
	obj = models.Register()
	obj.name = request.GET['name']
	obj.state = request.GET['state']
	obj.city = request.GET['city']
	obj.contact = request.GET['contact']
	obj.password = request.GET['password']
	obj.save()
	return render(request,'save.html')

def view(request):
	context = {
	'data1' : models.Register.objects.all()
	}
	return render(request,'view.html',context)

def delete(request):
	if request.method == 'GET' and 'delete' in request.GET:
		dl(request)
		call = 'delete.html'
		context={}
	if request.method == 'GET' and 'update' in request.GET:
		call = 'create_sec.html'
		context={
		'id': models.Register.objects.get(id=request.GET['update']),
		}
	return render(request,call,context)

#supported Function of DELETE()
def dl(request):
	if request.GET['delete'] is not None and request.GET['delete'] != '':
	  		models.Register.objects.get(id=request.GET['delete']).delete()
 
