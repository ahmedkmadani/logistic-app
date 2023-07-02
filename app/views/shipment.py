from django.shortcuts import render, redirect
from app.forms.order_form import OrderForm
from app.models.order import Order, OrderStatus
from app.utils.order_pdf import generate_order_pdf
from app.models.shippment import Shipment, ShipmentStatus


def shipment(request):
    data = Shipment.objects.all()
    status = ShipmentStatus.objects.all()
    return render(request, "dashboard/shipment.html", {"data": data, "status": status})

def update_shipment(request, pk):
    if request.method == 'POST':
        status_id = request.POST.get('status')
        try:
            order = Order.objects.get(pk=pk)
            status = OrderStatus.objects.get(pk=status_id)
            order.status = status
            order.save()
            if order.status.status == "In Warehouse":
                Shipment.objects.create(order=order)
            return redirect('order')
        except Order.DoesNotExist:
            pass
    return redirect('order')  