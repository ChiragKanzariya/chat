from django.shortcuts import render
#from .models import UserData

# Create your views here.
def create(request):
	
	return render(request,'create.html',{})

def save(request):
	c = UserData()
	c.name = request.POST.get("name")
	c.state = request.POST['state']
	c.city = request.POST['city']
	c.contact = request.POST['contact']
	c.password = request.POST['password']
	c.save()

	return render(request,'save.html',{'name' : request.POST['name']})