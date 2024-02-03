from django.utils import timezone

from django.shortcuts import render, get_object_or_404

from blog.models import Post


# Create your views here.


def blog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    post = get_object_or_404(posts)
    contex = {'post': post}
    return render(request, 'blog/single-blog.html', contex)


def single_blog(request, pid):
    post = get_object_or_404(Post, pk=pid)
    post.count_views += 1
    post.save()
    contex = {'post': post}
    return render(request, 'blog/single-blog.html', contex)
