
from django.urls import path
from app import views
urlpatterns = [
     path('', views.todoList, name='todoList'),
     path('todo_create/', views.todoCreate, name='todoCreate'),
     path('todoDelete/<int:pk>/', views.todoDelete, name='todoDelete'),
     path('todoUpdate/<int:pk>/', views.todoUpdate, name='todoUpdate'),
    
]
