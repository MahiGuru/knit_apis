from django.db import models
from .timestamp_model import TimestampedModel
from .category_model import Category
import re
from .image_model import PImage

class SubCategory(TimestampedModel):
    name = models.CharField(max_length=50, default=None)
    code = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=120, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, default=None)
    images = models.ForeignKey(PImage, on_delete=models.CASCADE,blank=True, default=None, null=True)

    class Meta:
        db_table = 'subcategorys'
        managed = True

    def save(self, *args, **kwargs):
        if not self.name:
            raise ValueError("Please enter sub-category name")
        else:
            replaced_txt = re.sub(r'\W+', '_', self.name)
            self.code = replaced_txt.upper()
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

