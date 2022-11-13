from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=31)
    image = models.ImageField(upload_to='category_img/')

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='f_category')
    name = models.CharField(max_length=31)
    image = models.ImageField(upload_to='sub_category_img/')

    def __str__(self):
        return self.name
