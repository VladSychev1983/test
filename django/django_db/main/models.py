from django.db import models

class Phones(models.Model):
    id = models.BigIntegerField(primary_key=True,null=False)
    name = models.CharField(max_length=50,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    image = models.URLField(max_length=200,null=True)
    #datetime.date.today() = 2024-08-09
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50,null=True)

