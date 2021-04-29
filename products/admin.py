from django.contrib import admin
from .p_models.image_model import PImage
from .p_models.category_model import Category
from .p_models.sub_category_model import SubCategory

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(PImage)