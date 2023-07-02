from django.shortcuts import render, redirect
from app.models.region import Region
from app.forms.region_form import RegionForm


def region(request):
    data = Region.objects.all()
    if request.method == "POST":
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("region")
    else:
        form = RegionForm()
    return render(request, "dashboard/region.html", {"form": form, "data": data})
