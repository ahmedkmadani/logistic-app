from django import forms
from app.models.buisness import Business
from app.models.neighborhood import Neighborhood


class BusinessForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Enter business name"}),
    )
    address = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Enter business address"}),
    )
    phone_number = forms.CharField(
        max_length=255,
        widget=forms.NumberInput(attrs={"placeholder": "Enter business phone number"}),
    )
    email = forms.CharField(
        max_length=255,
        widget=forms.EmailInput(attrs={"placeholder": "Enter business email"}),
    )

    class Meta:
        model = Business
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
