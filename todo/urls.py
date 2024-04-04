from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasklist, name='list'),  # /: shows the list of all tasks
    path('add/', views.taskadd, name='add'),   # /add: adds a new task
    path('edit/<pk>/', views.taskadd, name='edit'),   # /add: adds a new task
    path('delete/<pk>/', views.taskdelete, name='delete'),   # /add: adds a new task
    path('operate/<pk>/', views.taskoperation, name='operate'),   # /add: adds a new task
]
