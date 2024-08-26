# from django.shortcuts import render
# from machina.models import Forum
# # Create your views here.


# def forum_home(request):
#         forums = Forum.objects.all()
#         return render(request, 'forum_app/forum_home.html', {'forums': forums})



from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Foruma, Post, Category, Comment
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm

def forum_list(request):
    forums = Foruma.objects.all()
    categories = Category.objects.all()
    return render(request, 'forum/forum_list.html', {'forums': forums, 'categories': categories})

def forum_detail(request, forum_id):
    forum = get_object_or_404(Foruma, pk=forum_id)
    posts = forum.post_set.all().order_by('-created_at')
    return render(request, 'forum/forum_detail.html', {'forum': forum, 'posts': posts})

@login_required
def post_create(request, forum_id):
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

@login_required
def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())  # Redirect back to the post
    else:
        form = CommentForm()
    return render(request, 'forum/comment_create.html', {'form': form, 'post': post})

@login_required
def post_create(request, forum_id):
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

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'forum/post_detail.html', {'post': post})