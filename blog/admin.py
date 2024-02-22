from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Post, Category


# Register your models here.
class postAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    date_hierarchy = 'published_date'
    empty_value_display = '-empty-'
    fields = ('title', 'published_date', 'content', 'author', 'image', 'category', 'tags', 'status', 'count_views')
    list_display = ('id', 'title', 'published_date', 'author', 'status', 'count_views', 'created_date', 'updated_date')
    list_filter = ('published_date', 'author', 'status', 'tags')
    search_fields = ('title', 'author', 'status', 'published_date')


class categoryAdmin(admin.ModelAdmin):
    fields = 'name'


admin.site.register(Post, postAdmin)
admin.site.register(Category)
