from typing import Any, Dict, Optional, Type, Union
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task

# Create your views here.

class CustomLoginView(LoginView):
    template_name: str='base/login.html'
    fields = '__all__'
    redirect_authenticated_user: bool = True
    
    def get_success_url(self) -> str:
        
        return reverse_lazy('tasks')


class TaskList(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'base/task_list.html'
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tasks']= context['tasks'].filter(user=self.request.user)
        context['count']= context['tasks'].filter(complete=False).count()
        return context

class TaskDetail(LoginRequiredMixin,DetailView):
    model= Task
    context_object_name: Optional[str] = 'task'
    template_name: str = 'base/task.html'


class TaskCreate(LoginRequiredMixin,CreateView):
    model: Type[Task] = Task
    fields = '__all__'
    success_url: Optional[str] = reverse_lazy('tasks')
        
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form=form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model: Type[Task]= Task
    fields = '__all__'
    success_url: Optional[str] = reverse_lazy('tasks')
    
class TaskDelete(LoginRequiredMixin,DeleteView):
    model: Type[Task]  = Task
    context_object_name: Optional[str] = 'task'
    success_url: Optional[str] = reverse_lazy('tasks')




    
    
 