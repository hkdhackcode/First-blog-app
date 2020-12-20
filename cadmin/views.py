from django.shortcuts import render, redirect, get_object_or_404, reverse
from blog.forms import PostForm
from django.contrib import messages
from blog.models import Post, Author, Category, Tag

# view to add post.

def post_add(request):

    # If request is POST, create a bound form(form with data)
    if request.method == "POST":
        f = PostForm(request.POST)

        # check whether form is vaid or not 
        # if form is valid, save the data to the database
        # and redirect the user back to the add post form

        # if for is invalid show form with error again 
        if f.is_valid():
            # save data
            f.save()
            # show message when post add
            messages.add_message(request, messages.INFO, 'Post added.')
            return redirect('post_add')
    # if request is GET the show unbound form to the user
    else:
        f = PostForm()
    return render(request, 'cadmin/post_add.htm', {'form':f})        


# view to update post.

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # if request is POST, createa bound form(form with data)
    if request.method == "POST":
        f = PostForm(request.POST, instance=post)

        # check whether from is valid or not
        # if the form is valid, save the data to the database
        # and redirect the user back to the update post form 

        #if form is invalid show form with error again
        if f.is_valid:
            f.save()
            messages.add_message(request, messages.INFO, 'Post updated.')
            return redirect(reverse('post_update', args=[post.id]))

    #if request is GET , then show unbound from to the user, along with the data
    else:
        f = PostForm(instance=post)

    return render(request, 'cadmin/post_update.htm', {'form':f})