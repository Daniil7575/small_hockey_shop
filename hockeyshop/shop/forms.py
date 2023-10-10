from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    # image = 
    class Meta:
        model = Item
        fields = [
            "title",
            "description",
            "price",
            "location",
            "quantity",
            "image"
        ]
