from django.contrib import admin

# Register your models here.
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'social_media')
admin.site.register(Contact, ContactAdmin)