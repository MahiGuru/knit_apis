from django.db import models
from .timestamp_model import TimestampedModel
import re
from .image_model import PImage

class Brand(TimestampedModel):
    name = models.CharField(max_length=40, default=None)
    code = models.CharField(max_length=40, default=None)
    description = models.CharField(max_length=120, default=None)
    images = models.ForeignKey(PImage, on_delete=models.CASCADE, blank=False, default=None)
    
    class Meta:
        db_table = 'brands'
        managed = True

    def save(self, *args, **kwargs):
        if not self.name:
            raise ValueError("Please enter brand name")
        else:
            replaced_txt = re.sub(r'\W+', '_', self.name)
            self.code = replaced_txt.upper()
        
        super().save(*args, **kwargs)
    
    # def __str__(self):
    #     return self.code








