from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_('Name'), max_length=255, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    taste = models.CharField(_('Taste'), max_length=255, null=False, blank=False)
    description = models.TextField(_('Description'), blank=True, null=True)
    is_active = models.BooleanField(_('Is active'), default=True)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    objects = ProductManager()

    def __str__(self):
        return self.name + ' ' + str(self.category)