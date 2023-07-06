from django.contrib import admin

# Register your models here.
from app.models.buisness import Business
from app.models.driver import Driver
from app.models.neighborhood import Neighborhood
from app.models.order import Order, OrderStatus
from app.models.region import Region
from app.models.shippment import Shipment, ShipmentStatus

admin.site.register(Business)
admin.site.register(Driver)
admin.site.register(Neighborhood)
admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(Region)
admin.site.register(Shipment)
admin.site.register(ShipmentStatus)
