from django.db import models

# Create your models here.

app_name = 'crud'


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.name

