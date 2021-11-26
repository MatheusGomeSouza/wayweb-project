from django import forms
from django.conf import settings

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
PRODUCT_SIZE_NUMBER_CHOICES = (
    (1, "40"),
    (2, "42"),
    (3, "44"),
    (4, "46"),
)
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
    size_number = forms.TypedChoiceField(
        label="Numero", choices=PRODUCT_SIZE_NUMBER_CHOICES, coerce=int
    )
    # size = forms.TypedChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=PRODUCT_SIZE_CHOICES
    # )
    # size_number = forms.TypedChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=PRODUCT_SIZE_NUMBER_CHOICES
    # )
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )