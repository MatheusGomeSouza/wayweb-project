from django import forms
from django.conf import settings
from django.forms.widgets import RadioSelect

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
PRODUCT_SIZE_CHOICES = (
    (1, "P"),
    (2, "M"),
    (3, "G"),
    (4, "GG"),
)

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        label="Quantidade", choices=PRODUCT_QUANTITY_CHOICES, coerce=int
    )
    size = forms.TypedChoiceField(
        label="Tamanho", choices=PRODUCT_SIZE_CHOICES, coerce=int
    )
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )

class CartAddFreigth(forms.Form):
    cep = forms.TextInput()