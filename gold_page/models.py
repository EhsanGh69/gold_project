from django.db import models
from django.utils.html import format_html

from django_jalali.db import models as jmodels
from jdatetime import datetime



def products_image_path(instance, filename):
    file_ext = filename.split('.')[-1]
    time_str = str(datetime.now().time()).split('.')[0].replace(':', '_')
    return f"products_images/{instance.title}_{time_str}.{file_ext}"



class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان محصول')
    price = models.PositiveIntegerField(default=0, verbose_name='قیمت')
    product_img = models.ImageField(upload_to=products_image_path, verbose_name='تصویر')
    show_slider = models.BooleanField(default=False, verbose_name='نمایش در اسلایدر')
    create_date = jmodels.jDateField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    update_date = jmodels.jDateField(auto_now=True, verbose_name='تاریخ آخرین ویرایش')

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.title
    
    def product_img_tag(self):
        return format_html(f'''
            <a href='{self.product_img.url}'>
                <img src='{self.product_img.url}' width='100' height='75' style='border-radius: 5px;'>
            </a>
        ''')
    product_img_tag.short_description = "تصویر محصول"


