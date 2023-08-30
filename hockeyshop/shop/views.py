from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from shop.models import Item


class ShopHome(ListView):
    model = Item
    context_object_name = "items"
    template_name = "shop/home.html"

    def get_queryset(self) -> QuerySet[Any]:
        return Item.objects.all()


class ShopItemDetail(DetailView):
    model = Item
    template_name = "shop/item.html"
    context_object_name = "item"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["photos"] = ctx["item"].images.all()
        return ctx
