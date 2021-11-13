from django.db import models

# Create your models here.
class Product(models.Model):
    # objects = None
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

class StudentForm(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

class Introduction(models.Model):
    name = models.CharField(max_length=20)
    textarea = models.CharField(max_length=34)

    def __str__(self):
        return self.name
# class Meta:
#     name  = Product.product_name