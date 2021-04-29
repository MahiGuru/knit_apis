from django.db import models

from datetime import datetime
from django.utils.timezone import now

from .category_model import Category
from .image_model import PImage
from .sub_category_model import SubCategory
from .timestamp_model import TimestampedModel 
from .color_model import ColorModel
from .sizes_model import SizeModel
from .offers_model import OfferModel
from .brand_model import Brand

class Product(TimestampedModel):

    # Product basic info
    title = models.CharField(null=True, max_length=80,  default=None) 
    description = models.CharField(null=True, max_length=120,  default=None) 
    quantity =  models.IntegerField(blank=False, null=False, default=0)
    availability =  models.BooleanField(default=True, blank=True, null=True)
    price = models.FloatField(blank=False, null=False, default=0.00)
    age_group =  models.BooleanField(default=True, blank=True, null=True)

    # Product details
    images = models.ManyToManyField(PImage, blank=True, default=None)
    offers = models.ForeignKey(OfferModel, on_delete=models.CASCADE, blank=True, null=True)
    colors = models.ForeignKey(ColorModel, on_delete=models.CASCADE, blank=True, null=True)
    sizes = models.ForeignKey(SizeModel, on_delete=models.CASCADE, blank=True, null=True)
    
    #Categorys
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)

    #Product belongs to vendor
    user = models.IntegerField(blank=True, null=True) 

    class Meta:
        db_table = 'products'
        managed = True
    
    def __str__(self):
        return self.code

