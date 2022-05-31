from django.contrib import admin
from .models import Emails


class EmailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender_id', 'recipient_id', 'topic', 'date', 'is_deleted')
    search_fields = ('id', 'sender_id', 'recipient_id')


admin.site.register(Emails, EmailsAdmin)
