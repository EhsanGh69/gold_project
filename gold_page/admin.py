from django.contrib import admin

from django_jalali.admin.filters import JDateFieldListFilter

from .models import Product


admin.sites.AdminSite.site_header = "پنل ادمین موبایل گلد"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'product_img_tag', 'show_slider', 'create_date', 'update_date']
    ordering = ['create_date', 'title']
    list_filter = ['title', ('create_date', JDateFieldListFilter)]
    search_fields = ['title']

