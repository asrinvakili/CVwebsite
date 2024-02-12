from django.http import Http404
from django.utils import timezone

from django.shortcuts import render, get_object_or_404

from blog.models import Post

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


def blog(request, **kwargs):
    posts = Post.objects.filter(status=True, published_date__lte=timezone.now())
    if kwargs.get('cat_name') is not None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_user') is not None:
        posts = posts.filter(author__username=kwargs['author_user'])

    posts = Paginator(posts, 3)
    try:
        page_numb = request.GET.get('page')
        posts = posts.get_page(page_numb)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def single_blog(request, post_id):
    posts = Post.objects.filter(status=True, published_date__lte=timezone.now())
    post = get_object_or_404(posts, pk=post_id)
    post.count_views += 1

    if post_id < len(posts):
        next_post = posts[post_id + 1]
    else:
        next_post = None
    if post_id > 1:
        prev_post = posts[post_id - 1]
    else:
        prev_post = None

    context = {
        'post': post,
        'next_post': next_post,
        'prev_post': prev_post
    }

    return render(request, 'blog/single-blog.html', context)


def blog_search(request):
    posts = Post.objects.filter(status=True, published_date__lte=timezone.now())
    if request.method == 'GET':
        posts = posts.filter(content__contains=request.GET.get('s'))
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)
