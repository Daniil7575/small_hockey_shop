from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path("<int:pk>/", views.ShopItemDetail.as_view(), name="item_detail"),
    path("", views.ShopHome.as_view(), name="home"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

