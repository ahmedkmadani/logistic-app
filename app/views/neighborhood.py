from django.shortcuts import render, redirect
from app.models.neighborhood import Neighborhood
from app.forms.neighborhood_form import NeighborhoodForm


def neighborhood(request):
    data = Neighborhood.objects.all()
    if request.method == "POST":
        form = NeighborhoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("neighborhood")
    else:
        form = NeighborhoodForm()
    return render(request, "dashboard/neighbourhood.html", {"form": form, "data": data})
