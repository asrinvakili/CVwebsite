from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.utils import timezone

from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "Blog Newest"
    link = "/rss/feed"
    description = "Newest Post From Blog"

    def items(self):
        return Post.objects.filter(status=True, published_date__lte=timezone.now())

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)
