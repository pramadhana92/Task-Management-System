from django.urls import path

from . import views

urlpatterns = [
    path('api', views.TaskListAPI.as_view(), name='task-list'),
    path('api/<int:task_id>/', views.TaskDetailAPI.as_view(), name='task-detail'),
]