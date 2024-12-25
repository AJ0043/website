from django.contrib import admin

# Register your models here.
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone', 'Business', 'Service', 'Message')