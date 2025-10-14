from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=200)
    description = RichTextField()
    has_fixed_price = models.BooleanField(default=True)
    fixed_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

