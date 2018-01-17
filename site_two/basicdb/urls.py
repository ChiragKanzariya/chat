from django.urls import path
from basicdb import views
urlpatterns = [
	path('create/',views.create,name='create'),
	path('save/',views.save,name='save'),
	path('view/',views.view,name='view'),
	path('delete/',views.delete,name='delete'),
	path('create/',views.create,name='update'),
]