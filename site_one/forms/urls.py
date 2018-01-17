from django.urls import path
from . import views

urlpatterns = [
	path('forms/',views.index,name='index'),
	path('sec/',views.second,name='second'),
	path('show/',views.show,name='show'),
	path('delete/',views.delete,name='delete')
]