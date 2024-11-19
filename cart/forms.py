from django import forms


CAR_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddCarForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=CAR_QUANTITY_CHOICES,
        coerce=int,
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput,
    )
