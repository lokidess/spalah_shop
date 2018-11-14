from django.db import models

#  python manage.py makemigrations


class TradeMark(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Торговая Марка'
        verbose_name_plural = 'Торговые Марки'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    count = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products')  # install pillow for use ImageField (pip install pillow)
    trade_mark = models.ForeignKey(TradeMark, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    @property
    def total(self):
        return self.price * self.count
