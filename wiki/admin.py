from django.contrib import admin
from django.utils.html import format_html
from .models import Row, Column, WikiEntry


class RowAdmin(admin.ModelAdmin):
    pass

admin.site.register(Row, RowAdmin)


class ColumnAdmin(admin.ModelAdmin):
    pass

admin.site.register(Column, ColumnAdmin)


class WikiEntryAdmin(admin.ModelAdmin):
    pass

admin.site.register(WikiEntry, WikiEntryAdmin)
