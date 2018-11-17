from django.db import models

#  python manage.py makemigrations


class TradeMark(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Торговая Марка'
        verbose_name_plural = 'Торговые Марки'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Products(models.Model):

    STATUS_IN_STOCK = 0
    STATUS_OUT_STOCK = 1
    STATUS_PENDING = 2
    STATUS_NOT_PENDING = 3
    STATUS_DENY = 4

    STATUS_CHOICES = (
        (STATUS_IN_STOCK, 'В наличии'),
        (STATUS_OUT_STOCK, 'Нет в наличии'),
        (STATUS_PENDING, 'Ожидаеться'),
        (STATUS_NOT_PENDING, 'Не ожидаеться'),
        (STATUS_DENY, 'Снято с продаж'),
    )

    name = models.CharField(max_length=255)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=STATUS_IN_STOCK)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    count = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products')  # install pillow for use ImageField (pip install pillow)
    trade_mark = models.ForeignKey(TradeMark, on_delete=models.CASCADE)
    ordering = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    @property
    def total(self):
        return self.price * self.count
