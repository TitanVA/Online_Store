from django.contrib import admin
from django.forms import ValidationError
from .models import *
from PIL import Image


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    MIN_RESOLUTION = ("4000", "4000")

    list_display = ["title", "category", "image", "price", "is_in_stock", "num_of_item"]
    list_filter = ["is_in_stock", ]
    search_fields = ("title", "description")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["image"].help_text = f"Загружайте изображения с разрешением от {'x'.join(self.MIN_RESOLUTION)}"
        return form

    def clean_image(self):
        image = self.cleaned_date["image"]
        img = Image.open(image)
        min_height, min_width = self.MIN_RESOLUTION
        if img.height < int(min_height) or img.width < int(min_width):
            raise ValidationError("Разрешение изображения меньше минимального")
        return image


@admin.register(Review)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["date_created", "person_id", "product_id"]

admin.site.register(Category)
admin.site.register(OrderStage)
# admin.site.register(Review)
admin.site.register(ProductInCart)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderHistory)
