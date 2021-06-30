from django.contrib import admin

from .models import Category, Blog

class BlogAdmin(admin.ModelAdmin):
    list_display=('pk','title','content','category','postdate')

class CategoryAdmin(admin.ModelAdmin):
    list_display=('pk','category_name')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
