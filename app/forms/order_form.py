from django import forms
from app.models.order import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "recipient_name",
            "recipient_address",
            "sender",
            "recipient_region",
            "recipient_neighborhood",
            "recipient_phone_number",
            "recipient_email",
            "order_dimension",
            "weight",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
