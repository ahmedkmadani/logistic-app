from django.db import models
from app.models.region import Region
from app.models.neighborhood import Neighborhood


class Driver(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    driver_region = models.ForeignKey(
        Region, on_delete=models.SET_NULL, null=True, blank=True
    )
    driver_neighborhood = models.ForeignKey(
        Neighborhood, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @classmethod
    def driver_numbers(cls):
        return cls.objects.count()
