from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.generic import ListView, DetailView  # Corrected import path
from .models import Post


# def user_logins(request):
#     return render(request, 'authenticate/login.html', {})

# def user_home(request):
#     return render(request, 'authenticate/home.html', {})

# def user_contact(request):
#     return render(request, 'authenticate/contact.html', {}) 

class HomeView(ListView):
    model = Post
    template_name = 'home.html'