from django.urls import path
from blog.feeds import LatestEntriesFeed
from blog.views import blog, single_blog
from blog.sitemap import BlogSitemap

sitemaps = {'blog': BlogSitemap}
app_name = 'blog'

urlpatterns = [
    path('', blog, name='weblog'),
    path('<int:post_id>/', single_blog, name='singleblog'),
    path('category/<str:cat_name>/', blog, name='category'),
    path('author/<str:author_user>/', blog, name='author'),
    path('search/', blog, name='search'),
    path('rss/feed/', LatestEntriesFeed()),
    path('tag/<str:tag_name>/', blog, name='tag'),
]
