from django.db import models
from app.models.driver import Driver
from app.models.order import Order
from django.utils.crypto import get_random_string


class ShipmentStatus(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned'),
    )

    status = models.CharField(max_length=255, choices=STATUS_CHOICES)

    def __str__(self):
        return self.status


class Shipment(models.Model):
    shipment_number = models.CharField(max_length=20, unique=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True)
    shipment_status = models.ForeignKey(ShipmentStatus, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.shipment_status:
            self.shipment_status = ShipmentStatus.objects.get(status='Pending')

    def save(self, *args, **kwargs):
        if not self.shipment_number:
            self.shipment_number = self.generate_shipment_number()
        super().save(*args, **kwargs)

    def generate_shipment_number(self):
        random_code = get_random_string(length=8)
        return f"SH{random_code}"
