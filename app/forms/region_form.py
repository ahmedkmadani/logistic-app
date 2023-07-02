from django import forms
from app.models.region import Region


class RegionForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Enter region name"}),
    )
    code = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Enter region code"}),
    )

    class Meta:
        model = Region
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
