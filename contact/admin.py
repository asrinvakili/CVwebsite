from django.contrib import admin
from contact.models import Contact


# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'subject', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')


admin.site.register(Contact, contactAdmin)
