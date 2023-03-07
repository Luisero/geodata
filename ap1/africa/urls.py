from . import views
from django.urls import path

urlpatterns = [
    path('', views.index_africa, name='index-africa'),
    path('quenia', views.quenia, name='quenia'),
    path('angola', views.angola, name='angola')
]