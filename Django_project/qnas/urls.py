from django.urls import path
from . import views

app_name='qnas'
urlpatterns = [
    path('', views.index, name='index'),
    
]
