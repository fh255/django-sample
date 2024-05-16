from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.generic import ListView, DetailView , CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditForm


class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleView(DetailView):
     model = Post
     template_name = 'article.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ('title', 'title_tag', 'body')