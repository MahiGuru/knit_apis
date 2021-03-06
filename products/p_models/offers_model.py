from django.db import models 
from .choices_model import DISCOUNT_TYPE_CHOICES

class OfferModel(models.Model):
    title = models.CharField(null=True, max_length=80,  default=None)
    code = models.CharField(null=True, max_length=80, default=None, unique=True)
    discount = models.CharField(null=True, max_length=120,  default=None) 
    from_date = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    to_date = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    is_active = models.BooleanField(default=False, null=False, blank=False)
        
    class Meta:
        db_table = 'offers'
        managed = True
        verbose_name = 'Product Offers'
    
    def __str__(self):
        return self.code

