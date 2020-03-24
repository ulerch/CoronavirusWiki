from django.contrib import admin
from django.utils.html import format_html
from .models import Register, Row, Column, WikiEntry


class RegisterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Register, RegisterAdmin)


class RowAdmin(admin.ModelAdmin):
    pass

admin.site.register(Row, RowAdmin)


class ColumnAdmin(admin.ModelAdmin):
    pass

admin.site.register(Column, ColumnAdmin)


class WikiEntryAdmin(admin.ModelAdmin):
    pass

admin.site.register(WikiEntry, WikiEntryAdmin)
