from django import template
from blog.models import Post, Category, Comment
from django.utils import timezone

register = template.Library()


@register.inclusion_tag('blog/tags/last_post.html')
def last_post(arg=4):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/tags/post_categories.html')
def post_categories():
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    category = Category.objects.all()
    cat_dict = {}
    for name in category:
        cat_dict[name] = posts.filter(category=name).count
    return {'category': cat_dict}


@register.inclusion_tag('blog/tags/blog_categorie.html')
def blog_last_posts(arg=3):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/tags/home_blog.html')
def home_blog(arg=6):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('published_date')[:arg]
    return {'posts': posts}


@register.simple_tag(name='commentcount')
def function(pid):
    post = Post.objects.get(id=pid)
    return Comment.objects.filter(post=post.id, approved=True).count()
