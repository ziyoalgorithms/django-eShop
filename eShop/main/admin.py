from django.contrib import admin

from main import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {'slug': ['name', ]}


class ImageAdmin(admin.StackedInline):
    model = models.Image


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]
    list_display = ['id', 'name', 'category', 'price']
    list_filter = ['category__name', 'price']
    prepopulated_fields = {'slug': ['name']}


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product']
    list_filter = ['product__name']
