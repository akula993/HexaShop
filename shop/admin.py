from django.contrib import admin
# Register your models here.
from django.utils.safestring import mark_safe

from shop.models import Product, Category, ProductImage


class ProductInLine(admin.TabularInline):
    model = ProductImage
    extra = 0

    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = "Изоброжение"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    list_display = ('id', 'title', 'slug',)
    list_display_links = ('id', 'title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductInLine, ]
    list_display = ('id', 'title', 'price', 'category',)
    list_display_links = ('id', 'title',)
    list_editable = ('price', 'category',)
    list_filter = ('category',)
    search_fields = ('title', 'category__title')
    save_as = True
    save_on_top = True
    fieldsets = (
        ('Характеристики товара', {
            'fields': (('title', 'slug'), ('price', 'category'), 'description')
        }),
    )

# @admin.register(ProductImage)
# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = ('id', 'image', 'product', 'get_image')
#
#     list_display_links = ('id', 'image',)
#     readonly_fields = ('get_image',)
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.image.url} width="50" height="60">')
#
#     get_image.short_description = "Изоброжение"
