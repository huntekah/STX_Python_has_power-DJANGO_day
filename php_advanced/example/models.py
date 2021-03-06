from django.db import models
from datetime import datetime

# Create your models here.


class GiftList(models.Model):
    name = models.CharField(max_length=64)
    created_on = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

class Gift(models.Model):
    name = models.CharField(max_length=128)
    gift_list = models.ForeignKey(
        GiftList,
        related_name="gift",
        on_delete=models.CASCADE)

    def __str__(self):
        return self.name
