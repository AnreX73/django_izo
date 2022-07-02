from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(unique=True, max_length=100, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name
