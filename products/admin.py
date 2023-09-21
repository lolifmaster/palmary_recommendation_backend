from django.contrib import admin
from products.models import Product, Category, Type
from django.utils.translation import gettext_lazy as _

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'type', 'is_active', 'created_at', 'updated_at')
    list_filter = ('category', 'type', 'is_active')
    search_fields = ('name', 'category__name', 'type__name', 'description')
    list_editable = ('is_active',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


admin.site.site_header = _("Palmary Admin Panel")
admin.site.site_title = _("Palmary Admin Portal")
admin.site.index_title = _("Welcome to Palmary Researcher Portal")
