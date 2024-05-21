from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')
choice_list = [item for item in choices]

choice_list = []
for items in choices:
    choice_list.append(items)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value' : '', 'id': 'elder', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        # Updating the 'category' field's choices dynamically
        self.fields['category'].choices = Category.objects.all().values_list('name', 'name')

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),   
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            
        }

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.fields['category'].choices = Category.objects.all().values_list('name', 'name')
