from django.contrib import admin, messages

from shop.models import (
    Product,
    ProductImage,
    Attribute
)
from shop.filters import ProductStockFilter
# Register your models here.

# admin.site.register(Product)
# admin.site.register(ProductImage)
# admin.site.register(Attribute)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #inlines = [ProductImageInLine]
    search_fields = ('title', 'description',)
    list_filter = ("attributes", ProductStockFilter,)
    list_display = ('title', 'price', 'stock', 'images', 'get_attributes')
    actions = ('set_zero_stock',)

    @admin.display(description='Фото товара')
    def images(self, obj: Product):
        return list(obj.productimage_set.values_list('image', flat=True))

    @admin.display(description="Свойства")
    def get_attributes(self, obj: Product):
        return list(obj.attributes.all())

    @admin.action(description="Обнулить остатки")
    def set_zero_stock(self, request, queryset):
        queryset.update(stock=0)
        self.message_user(
            request=request,
            level=messages.SUCCESS,
            message="Остатки по товарам были обнулены")


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'product')

@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name',)