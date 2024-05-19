from django.urls import path
# from . import views
from .views import HomeView, ArticleView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView
urlpatterns = [
    # path('login/', views.user_logins, name='login'),  # Changed from views.login to views.user_logins
    # path('home/', views.user_home, name='home'),
    # path('contact/', views.user_contact, name='contact'),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleView.as_view(), name= "article"),
    path('add_post/', AddPostView.as_view(), name= "add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name= "update_post" ),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name= "delete_post" ),
    path('add_category/', AddCategoryView.as_view(), name="add_category")
]