from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.generic import ListView, DetailView  # Corrected import path
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleView(DetailView):
     model = Post
     template_name = 'article.html'