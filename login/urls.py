from django.urls import path
# from . import views
from .views import HomeView
urlpatterns = [
    # path('login/', views.user_logins, name='login'),  # Changed from views.login to views.user_logins
    # path('home/', views.user_home, name='home'),
    # path('contact/', views.user_contact, name='contact'),
    path('', HomeView.as_view(), name="home"),
]