from django.contrib import admin
from .models import Post, Kategoriya

#admin.site.register(Post)
admin.site.register(Kategoriya)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_kategoriya')
