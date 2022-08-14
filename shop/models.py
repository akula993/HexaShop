from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug_category": self.slug})


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(max_length=500, verbose_name='Описание', help_text='Максимум 500', null=True,
                                   blank=True)
    quotes = models.CharField(max_length=350, verbose_name='Цитата', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug_product": self.slug})


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product/', verbose_name='Картинка')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product', verbose_name='Продукт',
                                null=True, blank=True)
    style_active = models.CharField(max_length=50, blank=True, null=True, default='active')

    class Meta:
        verbose_name = 'Изоброжение'
        verbose_name_plural = 'Изоброжении'

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = "Изоброжение"
