from django.contrib import admin
from contact.models import Contact, NewsLetter


# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'subject', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')


class newsLetterAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_filter = ('email',)


admin.site.register(Contact, contactAdmin)
admin.site.register(NewsLetter, newsLetterAdmin)