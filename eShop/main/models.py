from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='category_img/')
    slug = models.SlugField(max_length=130)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:category_products', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=130)
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "product:product_detail",
            kwargs={
                "category_slug": self.category.slug,
                "product_slug": self.slug,
            }
        )


class Image(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='images',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to='product_img')

    def __str__(self):
        return self.product.name
