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
    all_posts = Post.objects.filter(status=True, published_date__lte=timezone.now())
    current_post = get_object_or_404(Post, pk=post_id)

    current_index = list(all_posts).index(current_post)

    next_index = current_index + 1 if current_index < len(all_posts) - 1 else None
    prev_index = current_index - 1 if current_index > 0 else None

    next_post = all_posts[next_index] if next_index is not None else None
    prev_post = all_posts[prev_index] if prev_index is not None else None

    context = {
        'post': current_post,
        'next_post': next_post,
        'prev_post': prev_post,
    }

    return render(request, 'blog/single-blog.html', context)
