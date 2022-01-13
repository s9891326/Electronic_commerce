from django.contrib import admin

from shop.models import Post, Product


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    search_fields = ['title']

admin.site.register(Post, PostAdmin)
admin.site.register(Product)
