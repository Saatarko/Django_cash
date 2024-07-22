from django.contrib import admin

from .models import Category, Posts


# Register your models here.
@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    list_display_links = ('id', 'title')  # поля по которым можно переходить в админке
    list_editable = ('content',)




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category', 'description_category')
    list_display_links = ('id', 'name_category')
    list_editable = ('description_category',)
