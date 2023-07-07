from app.models.order import Order
from app.models.shippment import Shipment, ShipmentStatus
from app.models.driver import Driver
from django.http import JsonResponse


def get_order_details(request, order_number):
    try:
        order = Order.objects.get(order_number=order_number)
        order_details = {
            "order_number": order.order_number,
            "recipient_name": order.recipient_name,
            "recipient_address": order.recipient_address,
            "recipient_neighborhood": order.recipient_neighborhood.name,
            "status": order.status.status,
        }
        return JsonResponse(order_details)
    except Order.DoesNotExist:
        return JsonResponse({"error": "Order not found"}, status=404)


def assgin_driver_order(request, order_number, driver_id):
    try:
        shipment = Shipment.objects.get(order__order_number=order_number)
        driver = Driver.objects.get(pk=driver_id)
        shipment.driver = driver
        shipment.shipment_status = ShipmentStatus.objects.get(status="Out for Delivery")
        shipment.save()
        return JsonResponse({"data": shipment.pk})
    except Shipment.DoesNotExist:
        return JsonResponse({"error": "shipment not found"}, status=404)


def get_driver_shipment(request, driver_id):
    try:
        shipments = Shipment.objects.filter(driver__pk=driver_id)
        data = [
            {
                "id": shipment.pk,
                "shipment_code": shipment.shipment_number,
                "shipment_status": shipment.shipment_status.status,
                "order_code": shipment.order.order_number
            }
            for shipment in shipments
        ]
        return JsonResponse({"data": data})
    except Shipment.DoesNotExist:
        return JsonResponse({"error": "shipment not found"}, status=404)
