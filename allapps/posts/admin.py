from django.contrib import admin
from .models import Post, Comment


def mark_as_active(modeladmin, request, queryset):
    queryset.update(active=True)
    mark_as_active.short_description = "Mark selected comments as active"

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')
    prepopulated_fields = {'slug': ('title', 'author',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created')
    actions = [mark_as_active]
