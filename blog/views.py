from django.http import Http404
from django.utils import timezone

from django.shortcuts import render, get_object_or_404

from blog.models import Post


# Create your views here.


def blog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def single_blog(request, post_id):
    posts = Post.objects.filter(pk=post_id,published_date__lte=timezone.now())
    post = posts.first()
    post.count_views += 1
    post.save()
    context = {'post': post}
    return render(request, 'blog/single-blog.html', context)

