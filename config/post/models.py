from django.db import models
from django.urls import reverse


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.BigIntegerField(default=0)
    category = models.CharField(max_length=200)

    @property
    def get_item_id(self):
        return self.id

    def __str__(self):
        return self.name
