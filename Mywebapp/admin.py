from django.contrib import admin
from .models import PythonTopic,JavaTopic
# Register your models here.
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone', 'Business', 'Service', 'Message')


admin.site.register(PythonTopic)
admin.site.register(JavaTopic)