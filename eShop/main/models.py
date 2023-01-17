from django.db import models
from django.urls import reverse

# class Category(MPTTModel):
#     name = models.CharField(
#         verbose_name=_("Kategoiya nomi"),
#         help_text=_("Majburiy"),
#         max_length=255,
#         unique=True,
#     )
#     slug = models.SlugField(
#         verbose_name=_("Kategoriyaning URLdagi nomi"),
#         max_length=255,
#         unique=True,
#     )
#     parent = TreeForeignKey(
#         "self",
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True,
#         related_name="children",
#     )
#     is_active = models.BooleanField(default=True)
#     image = models.ImageField(upload_to='category_img/')

#     class MPTTMeta:
#         order_insertion_by = ["name"]

#     class Meta:
#         verbose_name = _("Kategoriya")
#         verbose_name_plural = _("Kategoriyalar")

#     def get_absolute_url(self):
#         return reverse("product:category_products", kwargs={"category_slug": self.slug})

#     def __str__(self):
#         return self.name


# class ProductType(models.Model):
#     name = models.CharField(
#         verbose_name=_("Mahsulot nomi"),
#         help_text=_("Majburiy"),
#         max_length=255,
#         unique=True,
#     )
#     is_active = models.BooleanField(default=True)

#     class Meta:
#         verbose_name = _("Mahsulot turi")
#         verbose_name_plural = _("Mahsulot turlari")

#     def __str__(self):
#         return self.name


# class ProductSpecification(models.Model):
#     product_type = models.ForeignKey(
#         ProductType,
#         on_delete=models.RESTRICT,
#     )
#     name = models.CharField(
#         verbose_name=_("Nomi"),
#         help_text=_("Majburiy"),
#         max_length=255,
#     )

#     class Meta:
#         verbose_name = _("Product Specification")
#         verbose_name_plural = _("Product Specifications")

#     def __str__(self):
#         return self.name


# class Product(models.Model):
#     product_type = models.ForeignKey(
#         ProductType,
#         on_delete=models.RESTRICT,
#     )
#     category = models.ForeignKey(
#         Category,
#         on_delete=models.RESTRICT,
#     )
#     name = models.CharField(
#         verbose_name=_("Nomi"),
#         help_text=_("Majburiy"),
#         max_length=255,
#     )
#     description = models.TextField(
#         verbose_name=_("Mahsulot haqida ma'lumot"),
#         help_text=_("Majburiy"),
#     )
#     slug = models.SlugField(max_length=255)
#     price = models.DecimalField(
#         verbose_name=_("Narx"),
#         help_text=_("99999999.99 gacha"),
#         error_messages={
#             "name": {
#                 "max_length": _("Narx 0 dan 99999999.99 gacha bo'lishi kerak!"),
#             },
#         },
#         max_digits=10,
#         decimal_places=2,
#     )
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ("-created_at", )
#         verbose_name = _("Mahsulot")
#         verbose_name_plural = _("Mahsulotlar")

#     def get_absolute_url(self):
#         return reverse(
#             "product:product_detail",
#             kwargs={
#                 "category_slug": self.category.slug,
#                 "product_slug": self.slug,
#             }
#         )


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
