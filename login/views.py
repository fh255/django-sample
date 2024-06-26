from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


def LikeView(request, pk):
   post = get_object_or_404(Post, id=request.POST.get('post_id'))
   post.likes.add(request.user)
   return HttpResponseRedirect(reverse('article', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        # stuff =get_object_or_404(Post, id=self.kwargs['pk'])
        # total_likes = stuff.total_likes()
        context["cat_menu"] = cat_menu
        # context["total_likes"] = total_likes
        # Assign total_likes based on the existence of 'pk' in self.kwargs
        context["total_likes"] = get_object_or_404(Post, id=self.kwargs['pk']).total_likes() if 'pk' in self.kwargs else None
        return context

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     # You can access the queryset here to perform any filtering or customization
    #     # For now, let's just return the queryset as is
    #     return queryset

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render (request, 'category_list.html', {'cat_menu_list': cat_menu_list})

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render (request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts':category_posts})

class ArticleView(DetailView):
     model = Post
     template_name = 'article.html'

     def get_context_data(self, *args, **kwargs):
      cat_menu = Category.objects.all()
      context = super(ArticleView,self).get_context_data(*args, **kwargs)
      context["cat_menu"] = cat_menu
      return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    #fields = ('title', 'body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ('title', 'title_tag', 'body')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

