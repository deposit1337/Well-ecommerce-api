from django.db import models


# Create your models here.

class Brand(models.Model):
    brand = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.brand


class Category(models.Model):
    category_name = models.CharField(max_length=100,default=None,null=True)
    category_picture = models.ImageField(upload_to='images/category-images/',default=None,null=True)
    broad_name = models.CharField(max_length=100,default=None,null=True)
    slug = models.SlugField(max_length=255, default=None, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class AdditionalPicture(models.Model):
    picture = models.ImageField(upload_to='images/additional_images/')

    class Meta:
        verbose_name = 'Дополнительное фото'
        verbose_name_plural = 'Дополнительные фото'


class Item(models.Model):
    full_name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    vendor = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    main_picture = models.ImageField(upload_to='images/')
    additional_pic = models.ManyToManyField(AdditionalPicture)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, null=True)
    slug = models.SlugField(max_length=255, default=None, null=True)
    in_stock = models.BooleanField(default=True)
    price = models.IntegerField( default=None, null=True)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.full_name
