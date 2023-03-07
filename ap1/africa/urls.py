from . import views
from django.urls import path

urlpatterns = [
    path('', views.index_africa, name='index-africa'),
    path('kenya', views.kenya, name='kenya'),
    path('angola', views.angola, name='angola')
]