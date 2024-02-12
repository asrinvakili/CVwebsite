from django.http import Http404
from django.utils import timezone

from django.shortcuts import render, get_object_or_404

from blog.models import Post


# Create your views here.


def blog(request, **kwargs):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    if kwargs.get('cat_name') is not None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_user') is not None:
        posts = posts.filter(author__username=kwargs['author_user'])
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def single_blog(request, post_id):
    posts = Post.objects.filter(status=True, published_date__lte=timezone.now())
    post = get_object_or_404(posts, pk=post_id)
    context = {
        'post': post
    }

    return render(request, 'blog/single-blog.html', context)


def blog_search(request):
    posts = Post.objects.filter(status=True, published_date__lte=timezone.now())
    if request.method == 'GET':
        posts = posts.filter(content__contains=request.GET.get('s'))
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)
