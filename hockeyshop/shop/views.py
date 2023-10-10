from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.views.generic import CreateView, DeleteView, DetailView, ListView

from shop.forms import ItemForm
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
        return ctx


class CreateItem(LoginRequiredMixin, CreateView):
    form_class = ItemForm
    template_name = "shop/post_create_item_form.html"
    login_url = "admin/accounts/login"

    def form_valid(self, form):
        item = form.save(commit=False)
        item.owner = self.request.user.profile
        item.save()
        return super(CreateItem, self).form_valid(form)


class DeleteItem(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = "/"
