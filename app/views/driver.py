from django.shortcuts import render, redirect
from app.forms.driver_form import DriverForm
from app.models.driver import Driver


def driver(request):
    data = Driver.objects.all()
    if request.method == "POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("driver")
    else:
        form = DriverForm()
    return render(request, "dashboard/driver.html", {"form": form, "data": data})
