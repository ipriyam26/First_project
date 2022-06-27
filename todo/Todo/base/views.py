from typing import Optional, Type, Union
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Task
# Create your views here.

class TaskList(ListView):
    model = Task
    template_name = 'base/task_list.html'
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model= Task
    context_object_name: Optional[str] = 'task'
    template_name: str = 'base/task.html'

class TaskCreate(CreateView):
    model: Type[Task] = Task
    fields = '__all__'
    success_url: Optional[str] = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model: Type[Task]= Task
    fields = '__all__'
    success_url: Optional[str] = reverse_lazy('tasks')
    
    
 