from django.urls import path
from .views import *


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('create/', TaskCreate.as_view(), name='task-create'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task-detail'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task-update')
]