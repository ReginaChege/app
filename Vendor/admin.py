from django.contrib import admin
from .models import Vendor
# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    total_display = ("first_name","second_name","age","gender")
admin.site.register(Vendor,VendorAdmin)