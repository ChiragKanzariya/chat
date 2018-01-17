from django.urls import path
from example import views

urlpatterns = [
    path('example/', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
  	path('second/',views.SecondPage.as_view(),name='sec')
]