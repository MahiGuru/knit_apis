from django.db import models


class ProductOrder(TimestampedModel):
    class Meta:
            db_table = 'knit_order_product'
            managed = True