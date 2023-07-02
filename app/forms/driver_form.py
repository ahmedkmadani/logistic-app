from django import forms
from app.models.driver import Driver


class DriverForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Enter driver name"}),
    )
    address = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Enter driver address"}),
    )
    phone_number = forms.CharField(
        max_length=255,
        widget=forms.NumberInput(attrs={"placeholder": "Enter driver phone number"}),
    )
    email = forms.CharField(
        max_length=255,
        widget=forms.EmailInput(attrs={"placeholder": "Enter driver email"}),
    )

    class Meta:
        model = Driver
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
