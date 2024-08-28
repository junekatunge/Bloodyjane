# from django.shortcuts import render
# from machina.models import Forum
# # Create your views here.


# def forum_home(request):
#         forums = Forum.objects.all()
#         return render(request, 'forum_app/forum_home.html', {'forums': forums})

# This block is commented out, but it seems to be an attempt to create a basic forum view. It's likely using the machina library, which is a separate forum framework for Django. Since you are creating a custom forum, this block can be ignored for now.

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Foruma, Post, Category, Comment
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm

# This imports necessary modules for creating views and handling requests in Django.

def forum_list(request):
    forums = Foruma.objects.all()  # Get all forums from the database
    categories = Category.objects.all()  # Get all categories from the database
    return render(request, 'forum/forum_list.html', {'forums': forums, 'categories': categories})

# This view function renders the forum list page. It retrieves all forums and categories from the database and passes them to the 'forum/forum_list.html' template for display.

def forum_detail(request, forum_id):
    forum = get_object_or_404(Foruma, pk=forum_id)  # Get the forum object with the specified ID
    posts = forum.post_set.all().order_by('-created_at') # Get posts for this forum, sorted by creation date in descending order
    return render(request, 'forum/forum_detail.html', {'forum': forum, 'posts': posts})

# This view function renders the details of a specific forum. It retrieves the forum object using the 'forum_id' from the URL and all the posts associated with that forum. It then renders the 'forum/forum_detail.html' template with the forum and posts data.

@login_required
def post_create(request, forum_id):
    forum = get_object_or_404(Foruma, pk=forum_id) # Get the forum object for the specified forum ID
    if request.method == 'POST': # If the request method is POST (meaning the form was submitted)
        form = PostForm(request.POST) # Create a form instance with the POST data
        if form.is_valid(): # Check if the form data is valid
            post = form.save(commit=False) # Create a Post object from the form data, but don't save to the database yet
            post.author = request.user # Set the author of the post to the currently logged-in user
            post.forum = forum # Set the forum for this post
            post.save() # Save the post to the database
            return redirect('forum_detail', forum_id=forum_id) # Redirect to the forum details page after creating the post
    else: # If the request method is not POST (meaning the form is being displayed for the first time)
        form = PostForm() # Create an empty form
    return render(request, 'forum/post_create.html', {'form': form, 'forum': forum}) 

# This view function handles creating a new post within a forum. It checks for POST requests, validates the form data, and saves the new post to the database. It also allows rendering a blank form for creating a post.

@login_required
def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id) # Get the post object based on the post ID
    if request.method == 'POST': # If the form was submitted
        form = CommentForm(request.POST) # Create a form instance with POST data
        if form.is_valid(): # Check for form validation
            comment = form.save(commit=False) # Create a Comment object but don't save to the database yet
            comment.author = request.user # Set the author of the comment to the current user
            comment.post = post # Associate the comment with the correct post
            comment.save() # Save the comment to the database
            return HttpResponseRedirect(post.get_absolute_url()) # Redirect back to the post details page
    else: # If the form is being displayed for the first time
        form = CommentForm() # Create an empty form
    return render(request, 'forum/comment_create.html', {'form': form, 'post': post}) 

# This view function handles creating comments on existing posts. It handles POST requests, validates comment forms, and saves comments to the database. It also allows rendering a blank comment form.

@login_required
def post_create(request, forum_id): # This function is duplicated from the previous post_create definition
    forum = get_object_or_404(Foruma, pk=forum_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.forum = forum
            post.save()
            return redirect('forum_detail', forum_id=forum_id)
    else:
        form = PostForm()
    return render(request, 'forum/post_create.html', {'form': form, 'forum': forum})

# This function is a duplicate of the previous post_create function. It seems there might be a mistake in the code, as it's creating the same function twice.


# def post_detail(request, post_id):
#     post = get_object_or_404(Post, pk=post_id) # Get the Post object for the specified post ID
#     return render(request, 'forum/post_detail.html', {'post': post}) # Render the post details template with the post data

# This view function renders the details of a specific post. It retrieves the post object based on the 'post_id' from the URL and then renders the 'forum/post_detail.html' template with the post data.

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comment_set.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()
    return render(request, 'forum/post_detail.html', {'post': post, 'comments': comments, 'form': form})