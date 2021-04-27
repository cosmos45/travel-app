from django.db import models


class Food(models.Model):
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images', default=0)
    cost_for_2 = models.CharField(max_length=500)
    restaurant = models.CharField(max_length=500)
    must_try = models.CharField(max_length=500)


    def __str__(self):
        return str(self.state)