from django import forms
from django.core.exceptions import ValidationError
from .models import Author, Tag, Category, Post, Feedback
from django.template.defaultfilters import slugify


# form for author

class Authorform(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'

    # function to get clean name
    # restrict user to enter 'admin' and 'author' in author name
    # and store then in lower case

    def clean_name(self):
        name = self.cleaned_data.get('name')
        name_l = name.lower()
        if name_l == 'author' or name_l == 'admin':
            raise ValidationError(" Author name can't be 'admin/author' ")
        return name_l

    # function to store email in lower case 

    def clean_email(self):
       return self.cleaned_data.get('email').lower()
       

# form for tag

class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'
    
    def clean_name(self):
        n = self.cleaned_data.get('name')
        new = n.lower()
        if new == "tag" or new == "add" or new == "update":
            raise ValidationError("Tag name can't be '{}'".format(n))
        return new
    
    def clean_slug(self):
        return self.cleaned_data.get('slug').lower()


# form for category

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
    
    def clean_name(self):
        n = self.cleaned_data.get('name')
        new = n.lower()
        if new == "tag" or new == "add" or new == "update":
            raise ValidationError("Category name can't be '{}'".format(n))
        return new
    
    def clean_slug(self):
        return self.cleaned_data.get('slug').lower()

# form for post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'category', 'tags',)
    
    def clean_title(self):
        n = self.cleaned_data.get('title')
        new = n.lower()
        if new == "post" or new == "add" or new == "update":
            raise ValidationError("Post name can't be'{}'".format(n))
        return new
    
    def clean(self):
        cleaned_data = super(PostForm, self).clean()# call the parent clean method
        title = cleaned_data.get('title')
        # if title exists create slug from title
        if title:
            cleaned_data['slug'] = slugify(title)
        return cleaned_data

# form for feedback

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = '__all__'
