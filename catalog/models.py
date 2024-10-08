from decimal import Decimal
from django.db import models
from catalog.utils import upload_to


BLANK_NULL_TRUE = {"blank": True, "null": True}


class Category(models.Model):
    """
    A model for storing product categories.
    """

    name = models.CharField(
        max_length=50,
        verbose_name="Наименование категории",
        help_text="Наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории", help_text="Описание категории"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    """
    A model for storing information about products.
    """

    name = models.CharField(max_length=50, verbose_name="Наименование товара")
    description = models.TextField(**BLANK_NULL_TRUE, verbose_name="Описание товара")
    preview = models.ImageField(
        **BLANK_NULL_TRUE, upload_to=upload_to, verbose_name="Изображение товара"
    )
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00"),
        verbose_name="Цена за покупку",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name", "-price", "created_at", "-updated_at"]
