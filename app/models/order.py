from django.db import models
from django.utils.crypto import get_random_string
from app.models.buisness import Business
from app.models.region import Region
from app.models.neighborhood import Neighborhood



class OrderStatus(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Warehouse', 'In Warehouse'),
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned'),
    )

    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='Pending')


    def __str__(self):
        return self.status
    


class Order(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    recipient_name = models.CharField(max_length=255)
    recipient_address = models.CharField(max_length=255)
    sender = models.ForeignKey(Business, on_delete=models.CASCADE)
    recipient_region = models.ForeignKey(
        Region, on_delete=models.SET_NULL, null=True, blank=True
    )
    recipient_neighborhood = models.ForeignKey(
        Neighborhood, on_delete=models.SET_NULL, null=True, blank=True
    )
    recipient_phone_number = models.CharField(max_length=20, null=True)
    recipient_email = models.EmailField(max_length=255, null=True)
    order_dimension = models.CharField(max_length=255, null=True)
    weight = models.IntegerField(null=True)
    order_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

      
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.status_id:
            self.status_id = OrderStatus.objects.get(status='Pending').id

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self.generate_order_number()
        if not self.order_price:
            self.order_price = self.calculate_order_price()
        super().save(*args, **kwargs)

    def generate_order_number(self):
        random_code = get_random_string(length=8)
        return f"OD{random_code}"

    def __str__(self):
        return self.order_number

    @classmethod
    def order_numbers(cls):
        return cls.objects.count()
    

    def calculate_order_price(self):
        if self.recipient_region == self.sender.business_region:
            if self.weight <= 1:
                return 15
            else:
                extra_weight = self.weight - 1
                return 15 + (extra_weight * 2)
        elif self.recipient_region != self.sender.business_region:
            if self.weight <= 1:
                return 25
            else:
                extra_weight = self.weight - 1
                return 25 + (self.weight * 4)