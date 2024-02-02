from django.contrib import admin


# Register your models here.
class blogAdmin(admin.ModelAdmin):
    date_hierarchy = 'public_date'
    empty_value_display = '-empty-'
    fields = ('title', 'slug', 'public_date', 'content', 'author', 'tags')
    list_display = ('title', 'slug', 'public_date', 'author', 'tags')
    list_filter = ('public_date', 'author', 'status')
    search_fields = ('title', 'author', 'status', 'public_date')
