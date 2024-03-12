from django.urls import reverse
from django.contrib.sitemaps import Sitemap


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    prority = 0.5

    def items(self):
        return ['home:index']

    def location(self, items):
        return reverse(items)
