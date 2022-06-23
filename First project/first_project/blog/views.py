
from typing import Optional, Sequence, Union
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, 
                                  CreateView, 
                                  DetailView, 
                                  UpdateView, 
                                  DeleteView)
from .models import Post
from django.contrib.auth.models import User




def about(request:HttpRequest) ->HttpResponse : 
    return render(request, 'blog/about.html', {'title':'About'})

class PostListView(ListView):
    """Generate a list of all posts from the database
        to be displayed in the blog/home.html template
    """
    model = Post
    template_name = 'blog/home.html'
    context_object_name: Optional[str] = 'posts'
    ordering: Optional[Union[str, Sequence[str]]] = '-date_posted'
    paginate_by:int=5

class UserPostListView(ListView):
    """Generate a list of all posts from the database
        to be displayed in the blog/home.html template
    """
    model = Post
    template_name = 'blog/user_home.html'
    context_object_name: Optional[str] = 'posts'
    # ordering: Optional[Union[str, Sequence[str]]] = '-date_posted'
    paginate_by:int=5
    
    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted').order_by('-date_posted')
    

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url: Optional[str] = '/'
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

