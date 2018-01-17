from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def http(response):
	return HttpResponse("<h1> This is HttpResponse. </h1>")

'''
def render(request):
	t = loader.get_template('html/HttpResponse.html')
	return render(request,t)
	'''

def http2(response,username):
	return HttpResponse("<h1> This is HttpResponse = "+str(username)+"<h1>")

def http3(response):
	return HttpResponse("<script>alert('3rd')</script>")

