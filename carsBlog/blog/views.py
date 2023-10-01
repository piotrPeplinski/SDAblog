from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.http import Http404


def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'home.html', {'posts': posts})


def detail(request, post_id):
    # try:
    #     post = BlogPost.objects.get(id=post_id)
    # except BlogPost.DoesNotExist:
    #     raise Http404(f'No post with id {post_id} was found.')
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'detail.html', {'post': post})
