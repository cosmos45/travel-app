from django.db import models


class Guides(models.Model):
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images', default=0)


    def __str__(self):
        return str(self.state)