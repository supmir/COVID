from django.contrib import admin

# Register your models here.
from .models import Messages


class MessagesAdmin(admin.ModelAdmin):
    list_filter = ('verification', 'family', 'verified')
    list_display = ('name', 'verified', 'message')

admin.site.register(Messages, MessagesAdmin)
