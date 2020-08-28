from django.urls import path
from . import views

app_name='todo_app'
urlpatterns = [
    path('', views.list_tasks_item, name='list_tasks'),
    path('insert_task/', views.insert_tasks_item, name='insert_task'),
    path('delete_task/<int:task_id>/',
         views.delete_tasks_item, name='delete_task'),
]
