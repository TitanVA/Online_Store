import datetime

from django.db import models

from users.models import Customer


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class OrderStage(models.Model):
    name = models.CharField(max_length=50, verbose_name="Стадия заказа")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Стадия заказа'
        verbose_name_plural = "Стадии заказа"


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    title = models.CharField(max_length=250, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", null=True)
    image = models.ImageField(verbose_name="Изображение")
    price = models.PositiveIntegerField(verbose_name="Цена")
    is_in_stock = models.BooleanField(verbose_name="В наличии")
    num_of_item = models.PositiveIntegerField(verbose_name="Количество в наличии")
    days_for_production = models.PositiveIntegerField(verbose_name="Дней для изготовления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукты"
        ordering = ("title",)


class Review(models.Model):
    text = models.TextField(verbose_name="Текст отзыва")
    date_created = models.DateTimeField(default=datetime.datetime.now, verbose_name="Дата создания")
    photo = models.ImageField(verbose_name="Фото", blank=True, null=True)
    person_id = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Заказчик")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар", related_name="reviews")
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, related_name="children"
    )

    def __str__(self):
        return f"Отзыв о {self.product_id} - от пользователя {self.person_id}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class ProductInCart(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255, verbose_name="Наименование")
    product_price = models.PositiveIntegerField(verbose_name="Цена")
    num_of_products = models.PositiveIntegerField(default=1, verbose_name="Кол-во изделий")
    final_price = models.PositiveIntegerField(verbose_name="Общая цена")

    def __str__(self):
        return f"{self.product_id} x {self.product_price}"

    class Meta:
        verbose_name = "Продукт в корзине"
        verbose_name_plural = "Продукты в корзине"


class Cart(models.Model):
    person_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductInCart, blank=True)
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.PositiveIntegerField(verbose_name="Общая цена")
    is_active = models.BooleanField()

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class Order(models.Model):
    is_delivery = models.BooleanField()
    address = models.CharField(max_length=255)
    is_order = models.BooleanField()
    date_of_order = models.DateTimeField()
    purchase = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} - {self.address}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class OrderHistory(models.Model):
    person_id = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name="Покупатель")
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name="Заказ")
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Продукт")
    num_of_item = models.PositiveIntegerField(verbose_name="Кол-во")
    date_of_order = models.DateTimeField(verbose_name='Дата заказа')
    order_stage = models.ForeignKey(OrderStage, on_delete=models.PROTECT, verbose_name="Стадия заказа")

    def __str__(self):
        return f"{self.date_of_order} - {self.product_id} - {self.order_id}"

    class Meta:
        verbose_name = "История заказов"
        verbose_name_plural = "История заказов"
