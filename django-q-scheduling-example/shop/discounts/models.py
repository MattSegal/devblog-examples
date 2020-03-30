from django.db import models
from django.utils import timezone


class Discount(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField()

    def __str__(self):
        return f"Discount<{self.pk} - ${self.amount}>"
