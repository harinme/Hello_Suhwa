from django.urls import path
from . import views

app_name='qnas'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:qna_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:qna_pk>/delete/', views.delete, name='delete'),
    
]
