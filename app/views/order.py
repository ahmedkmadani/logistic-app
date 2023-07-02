from django.shortcuts import render, redirect
from app.forms.order_form import OrderForm
from app.models.order import Order, OrderStatus
from app.utils.order_pdf import generate_order_pdf
from app.models.shippment import Shipment


def order(request):
    data = Order.objects.all()
    status = OrderStatus.objects.all()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            pdf_filepath = generate_order_pdf(order)
            print(pdf_filepath)

            return redirect("order")
    else:
        form = OrderForm()
    return render(request, "dashboard/order.html", {"form": form, "data": data, "status": status})

def update_order(request, pk):
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