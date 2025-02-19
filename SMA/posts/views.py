from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def global_feed(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/global_feed.html', {'posts': posts})

@login_required
def user_profile(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'posts/user_profile.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('global_feed')
        else:
            messages.error(request, 'Error creating post. Please try again.')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})

@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('user_profile')
        else:
            messages.error(request, 'Error updating post. Please try again.')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/update_post.html', {'form': form})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('user_profile')
    return render(request, 'posts/delete_post.html', {'post': post})
