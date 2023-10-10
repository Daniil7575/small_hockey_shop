from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path("<int:pk>/", views.ShopItemDetail.as_view(), name="item_detail"),
    path("", views.ShopHome.as_view(), name="home"),
    path("create/", views.CreateItem.as_view(), name="create_item"),
    path("<int:pk>/delete/", views.DeleteItem.as_view(), name="delete_item")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
