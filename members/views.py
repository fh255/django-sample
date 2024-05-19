from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):  # Corrected CreateView
    form_class = UserCreationForm  # Corrected form_class
    template_name = 'registration/register.html'  # Corrected template_name
    success_url = reverse_lazy('login')
