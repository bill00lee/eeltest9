from django.db import models
from django.db.models.signals import pre_save, post_save
import random
import os

from .utils import unique_slug_generator

# Create your models here.
class Tow(models.Model):
        city            = models.CharField(max_length=120)
        slug            = models.SlugField(blank=True, unique=True)
        tow             = models.TextField()
        priceperkms     = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
        hook            = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
        dollies         = models.BooleanField(default=False)
        storage         = models.BooleanField(default=True)

        def __str__(self):
            return self.city

        def __unicode__(self):
            return self.city

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Tow)
