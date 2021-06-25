from django.urls import path
from . import views
from .views import index, updateTask, deleteTask


urlpatterns = [
    
    path('', index, name = 'task'),
    path('update-task/<int:id>/', updateTask, name = 'update_task'),
    path('delete-task/<int:id>/', deleteTask, name = 'delete_task'),
]