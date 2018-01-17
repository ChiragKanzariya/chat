from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('',views.http),
	#path('render/',views.render)
	#path('sec/',views.http2),
	path('3/',views.http3),
	#path('2/',views.http2),
	url(r'^(?P<username>\w+)$', views.http2,name='http2'),
]