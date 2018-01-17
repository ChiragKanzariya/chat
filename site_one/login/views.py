from django.shortcuts import render
from forms.models import RegisterForm as reg
# Create your views here.
def login(request):
	return render(request,"login/index.html")

def checker(request):
	user = request.GET['user']
	password = request.GET['pass']

	db = reg.objects.filter(firstname = user)

	return render(request,"login/checker.html",{"db":db })