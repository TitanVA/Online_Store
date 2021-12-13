from django.db import models


class Customer(models.Model):

    phone = models.CharField(max_length=20, verbose_name="Телефон")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    avatar = models.ImageField(blank=True, null=True)
    is_admin = models.BooleanField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
