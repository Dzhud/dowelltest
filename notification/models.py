from django.db import models
from django.utils import timezone


class Notification(models.Model):
    product_name = models.CharField(max_length=300)    
    url = models.URLField(max_length=200)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.product_name

