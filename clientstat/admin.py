from django.contrib import admin
from django.contrib.admin.decorators import register
from django.utils.html import format_html
from .models import Clients, Yandex, Comments



admin.site.index_template = 'admin/index.html'
admin.autodiscover()

@admin.register(Clients)
class ClientModelAdmin(admin.ModelAdmin,):
    prepopulated_fields = {'db_key':['username']}

@admin.register(Comments)
class CommentsNodelADmin(admin.ModelAdmin):
    list_display = ('comment_key', 'author_comment', 'comment_number')
    list_filter = ('comment_key',)

    

#admin.site.register(Comments)