from django.contrib import admin
from django.utils import timezone

from .models import Post


# def make_published(modeladmin, request, queryset):
#     queryset.update(published_date=timezone.now.strftime("%Y-%m-%d %H:%M:%S"))
# make_published.short_description = "Mark selected posts as published"


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('published_date', )
    search_fields = ('title', )
    readonly_fields = ('author', 'created_date')
    # actions = [make_published]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(Post, PostAdmin)
