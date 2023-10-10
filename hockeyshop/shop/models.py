from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # phone = PhoneNumberField(
    #     null=False, blank=False, unique=False, verbose_name="Телефон"
    # )
    phone = models.CharField(
        null=False, blank=False, unique=False, verbose_name="Телефон", max_length=12
    )
    tg_link = models.CharField(
        max_length=200, null=True, blank=True, unique=True, verbose_name="Телеграм"
    )
    whatsapp = models.CharField(
        max_length=150, null=True, blank=True, unique=True, verbose_name="Вотсап"
    )
    other_contacts = models.TextField(
        null=True, blank=True, verbose_name="Другие виды связи"
    )

    def __str__(self) -> str:
        return f"Профиль {self.user.username}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Item(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(max_length=600, blank=False, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="items")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    location = models.CharField(max_length=300, verbose_name="Локация")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    quantity = models.SmallIntegerField(default=1, verbose_name="Количество")
    image = models.ImageField(upload_to="images")

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.title}_{self.pk}"


# class ItemPhoto(models.Model):
#     item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="images")
#     image = models.ImageField(upload_to="images")

#     def __str__(self) -> str:
#         return f"Картинка {self.pk} для {self.item}"
