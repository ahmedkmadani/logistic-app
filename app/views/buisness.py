from django.shortcuts import render, redirect
from app.forms.business_form import BusinessForm
from app.models.buisness import Business
from app.models.neighborhood import Neighborhood
from django.http import JsonResponse


def buisness(request):
    data = Business.objects.all()
    if request.method == "POST":
        form = BusinessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("buisness")
    else:
        form = BusinessForm()
    return render(request, "dashboard/buisness.html", {"form": form, "data": data})


def get_neighborhoods(request):
    region_id = request.GET.get("region_id")
    neighborhoods = Neighborhood.objects.filter(region_id=region_id).values(
        "id", "name"
    )
    return JsonResponse({"neighborhoods": list(neighborhoods)})
