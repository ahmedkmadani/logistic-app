from app.models.order import Order
from django.http import JsonResponse

def get_order_details(request, order_number):
    try:
        order = Order.objects.get(order_number=order_number)
        # Retrieve other order details as needed
        order_details = {
            'order_number': order.order_number,
            'recipient_name': order.recipient_name,
            'recipient_address': order.recipient_address,
            'recipient_neighborhood': order.recipient_neighborhood.name,
            'status': order.status.status
        }
        return JsonResponse(order_details)
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)