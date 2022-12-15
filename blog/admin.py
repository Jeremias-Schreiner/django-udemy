from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modifield')
    list_display =('title', 'created', 'modifield')
    date_hierarchy = 'created'
    list_per_page = 10


# Register your models here.
admin.site.register(Post, PostAdmin)
