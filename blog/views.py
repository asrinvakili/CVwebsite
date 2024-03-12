from django.http import Http404
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from blog.forms import CommentForm
from blog.models import Post, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


def blog(request, **kwargs):
    posts = Post.objects.filter(status=True, published_date__lte=timezone.now())
    if kwargs.get('cat_name') is not None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_user') is not None:
        posts = posts.filter(author__username=kwargs['author_user'])
    if kwargs.get('tag_name') is not None:
        posts = posts.filter(tags__name__in=kwargs['tag_name'])

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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Comment Sent Successfully')
        else:
            messages.error(request, 'There was an error, Please try again')
    else:
        form = CommentForm()
    posts = Post.objects.filter(status=True, published_date__lte=timezone.now())
    post = get_object_or_404(posts, pk=post_id)
    post.count_views += 1
    post.save()
    current_post = Post.objects.get(pk=post_id)
    related_posts = Post.objects.filter(status=True, published_date__lte=timezone.now())
    next_post = related_posts.filter(id__gt=current_post.id).order_by('id').first()
    prev_post = related_posts.filter(id__lt=current_post.id).order_by('-id').first()
    comments = Comment.objects.filter(approved=True, post=post.id)
    context = {
        'post': post,
        'next_post': next_post,
        'prev_post': prev_post,
        'comments': comments,
        'form': form,
    }

    return render(request, 'blog/single-blog.html', context)


def blog_search(request):
    posts = Post.objects.filter(status=True, published_date__lte=timezone.now())
    if request.method == 'GET':
        posts = posts.filter(title__contains=request.GET.get('s'))
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)
