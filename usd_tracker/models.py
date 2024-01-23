from django.db import models


class ExchangeRate(models.Model):
    rate = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]
