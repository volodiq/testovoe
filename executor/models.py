from django.contrib.auth.models import User
from django.db import models


class ExecutorProfile(models.Model):
    """Профили исполнителей"""

    user = models.ForeignKey(
        User,
        related_name="executor_profile",
        on_delete=models.CASCADE,
    )
    experience = models.PositiveSmallIntegerField(
        verbose_name="Опыт в годах", default=0
    )
    phone = models.CharField(null=True, blank=True, max_length=30)

    class Meta:
        verbose_name = "Профиль исполнителя"
        verbose_name_plural = "Исполнители"

    def __str__(self):
        return self.user.username
