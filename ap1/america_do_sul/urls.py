from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_america, name='index-america'),
    path('brasil/', views.brasil, name='brasil'),
    path('chile/', views.chile, name='chile'),
    path('uruguai/', views.uruguai, name='uruguai')
]