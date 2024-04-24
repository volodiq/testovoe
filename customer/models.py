from django.contrib.auth.models import User
from django.db import models


class CustomerProfile(models.Model):
    """Профили заказчиков"""

    user = models.ForeignKey(
        User,
        related_name="customer_profile",
        on_delete=models.CASCADE,
    )
    phone = models.CharField(null=True, blank=True, max_length=30)

    class Meta:
        verbose_name = "Профиль заказчика"
        verbose_name_plural = "Заказчики"

    def __str__(self):
        return self.user.username
