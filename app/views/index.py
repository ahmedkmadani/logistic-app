from django.shortcuts import render
from app.models.order import Order
from app.models.buisness import Business
from app.models.driver import Driver
from app.models.region import Region
from django.db.models import Sum
from django.db.models.functions import ExtractMonth
from django import template
import json


def index(request):
    order_number = Order.order_numbers()
    business_number = Business.business_numbers()
    driver_number = Driver.driver_numbers()
    region_number = Region.region_numbers()

    monthly_totals = (
        Order.objects.annotate(month=ExtractMonth("created_at"))
        .values("month")
        .annotate(total_price=Sum("order_price"))
        .order_by("month")
    )
    price_data = [0] * 12
    for entry in monthly_totals:
        month = entry["month"]
        total_price = entry["total_price"]
        price_data[month - 1] = total_price

    data = {
        "order_number": order_number,
        "business_number": business_number,
        "driver_number": driver_number,
        "region_number": region_number,
    }

    return render(
        request, "dashboard/index.html", {"data": data, "price_data": price_data}
    )
