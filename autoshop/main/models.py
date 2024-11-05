from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(
        max_length=20,
        unique=True,
    )
    slug = models.SlugField(
        max_length=20,
        unique=True,
    )

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name


class Cars(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="cars",
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=50,
    )
    slug = models.SlugField(max_length=50)
    image = models.ImageField(
        upload_to="cars/%Y/%m/%d",
        blank=True,
    )
    description = models.TextField(
        blank=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    available = models.BooleanField(
        default=True,
    )
    created = models.DateField(
        auto_now_add=True,
    )
    updated = models.DateField(auto_now=True)
    discount = models.DecimalField(
        default=0.00,
        max_digits=4,
        decimal_places=2,
    )

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]
        verbose_name = "Машина"
        verbose_name_plural = "Машины"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("main:product_detail", args=[self.slug])

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price


class CarSpecifications(models.Model):
    car_id = models.ForeignKey(
        Cars,
        related_name="carspecifications",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=150)
    distance = models.IntegerField()
    engine_capacity = models.DecimalField(
        max_digits=2,
        decimal_places=1,
    )
    engine_power = models.IntegerField()
    type_engine = models.CharField(
        max_length=12,
        default="бензин",
    )
    owners = models.IntegerField()
    pts = models.CharField(max_length=12)
    customs = models.BooleanField(default=True)
    slug = models.SlugField(max_length=50)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]
        verbose_name = "Харрактреристика машины"
        verbose_name_plural = "Харрактреристики машин"

    def __str__(self) -> str:
        return self.name
