from django import forms
from app.models.neighborhood import Neighborhood


class NeighborhoodForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Enter Neighborhood name"}),
    )

    class Meta:
        model = Neighborhood
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
