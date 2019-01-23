from django.shortcuts import render, redirect
from .models import Post
from .forms import PostModelForm, CommentModelForm
from datetime import datetime

def index(request):
    context = {}
    posts = Post.objects.all()
    context['posts'] = posts
    return render(request, 'post/index.html', context)

def detail(request, post_id):
    context = {}
    context['posts'] = Post.objects.get(id=post_id)
    return render(request, 'post/detail.html', context)

def create(request):
    context = {}
    form = PostModelForm(request.POST)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('post:index')
        else:
            context['form'] = form
            return render(request, 'post/create.html', context)
    else:
        context['form'] = PostModelForm(initial={'date_created': datetime.now()})
        return render(request, 'post/create.html', context)

def comment(request, post_id):
    context = {}
    form = CommentModelForm(request.POST)
    context['form'] = CommentModelForm(initial={'date_created': datetime.now(), 'post': post_id})
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('post:index')
        else:
            context['form'] = form
            return render(request, 'post/create.html', context)
    else:
        context['form'] = CommentModelForm(initial={'date_created': datetime.now(), 'post': post_id})
        return render(request, 'post/create.html', context)

def update(request, post_id):
    context = {}
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponse('Post updated')
        else:
            context['form'] = form
            render(request, 'post/update.html', context)
    else:
        context['form'] = PostModelForm(instance=post)
    return render(request, 'post/update.html', context)
