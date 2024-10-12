from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'details', 'image', 'created_at', 'created_by']
    search_fields = ['title', 'details', 'category']
    readonly_fields = ['created_at']
    list_filter = ['created_at', 'created_by']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'content', 'created_at', 'user']
    search_fields = ['id', 'blog', 'content']
    readonly_fields = ['created_at']
    list_filter = ['created_at']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
# Register your models here.
