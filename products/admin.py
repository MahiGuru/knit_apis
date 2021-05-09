from django.contrib import admin
from .p_models.image_model import PImage
from .p_models.category_model import Category
from .p_models.sub_category_model import SubCategory
from .p_models.color_model import ColorModel
from .p_models.offers_model import OfferModel
from .p_models.product_model import Product
from .p_models.brand_model import Brand
from .p_models.sizes_model import SizeModel

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ColorModel)
admin.site.register(Product)
admin.site.register(OfferModel)
admin.site.register(Brand)
admin.site.register(SizeModel)
admin.site.register(PImage)