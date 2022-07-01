from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
  
    path('', views.saveuser, name='saveuser'),
    path('show', views.show, name='show'),

    
    
    
    
]