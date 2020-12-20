from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse
from .models import Author, Tag, Category, Post
from django.contrib import messages
from .forms import FeedbackForm
from firstapp import helpers



# view function to display a list of posts

def post_list(request):
    posts = Post.objects.order_by("-id").all()
    posts = helpers.pg_records(request, posts, 5)
    return render(request, 'blog/post_list.htm', {'posts':posts})

# view function to display a single post

def post_detail(request, pk, post_slug):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'blog/post_detail.htm', {'post':post})


# view function to display post by author

def post_by_author(request, pk, author_name):
    author = get_object_or_404(Author, pk = pk)
    posts = get_list_or_404(Post.objects.order_by("-id"), author__pk = pk)
    posts = helpers.pg_records(request, posts, 5)
    context = {
        'author' : author,
        'posts': posts
    }
    return render(request, 'blog/post_by_author.htm', context)
    

# view function to display post by category

def post_by_category(request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    posts =get_list_or_404(Post.objects.order_by("-id"), category__slug = category_slug)
    posts = helpers.pg_records(request, posts, 5)
    context = {
        'category': category,
        'posts': posts
    }
    
    return render(request, 'blog/post_by_category.htm', context)


# view function to display post by tag

def post_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug = tag_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), tags__slug = tag_slug)
    posts = helpers.pg_records(request, posts, 5) 
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/post_by_tag.htm', context)

# function to redirect

def test_redirect(request):
    c = Category.objects.get(name = 'python')
    return redirect(c)

# view to display feedback form

def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)

        # check the validation o form

        if f.is_valid():
            # if valid save the data to the data base
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('feedback')
    else:
        f = FeedbackForm()
    return render(request, 'blog/feedback.htm', {'form':f})
    