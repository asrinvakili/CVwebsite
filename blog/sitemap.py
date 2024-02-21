from django.contrib.sitemaps import Sitemap
from django.utils import timezone
from blog.models import Post


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    prority = 0.5

    def items(self):
        return Post.objects.filter(status=True, published_date__lte=timezone.now())

    def lastmod(self, obj):
        return obj.published_date

    def location(self, obj):
        return obj.get_absolute_url()
