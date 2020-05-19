from django.contrib import admin, messages

# Register your models here.
from .models import Messages
from django.utils.translation import ngettext


class MessagesAdmin(admin.ModelAdmin):
    def make_visible(self, request, queryset):
        updated = queryset.update(visible=True)
        self.message_user(request, ngettext(
            '%d message was successfully marked as visible.',
            '%d messages were successfully marked as visible.',
            updated,
        ) % updated, messages.SUCCESS)



    make_visible.short_description = "Mark selected messages as visible"

    def make_hidden(self, request, queryset):
        updated = queryset.update(visible=False)
        self.message_user(request, ngettext(
            '%d message was successfully marked as hidden.',
            '%d messages were successfully marked as hidden.',
            updated,
        ) % updated, messages.SUCCESS)
    make_hidden.short_description = "Mark selected messages as hidden"
    
    list_filter = ('verification', 'family', 'verified','visible')
    list_display = ('name', 'verified','visible', 'message')
    actions = ['make_visible','make_hidden']


admin.site.register(Messages, MessagesAdmin)
