from django import template
from blog.models import Post, Category

register = template.Library()


@register.inclusion_tag('blog/tags/last_post.html')
def last_post(arg=4):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/tags/post_categories.html')
def post_categories():
    posts = Post.objects.filter(status=1)
    category = Category.objects.all()
    cat_dict = {}
    for name in category:
        cat_dict[name] = posts.filter(category=name).count
    return {'category': cat_dict}
