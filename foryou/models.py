from django.db import models


class State(models.Model):
    state = models.CharField(max_length=100)
    no_of_cities = models.CharField(max_length=500)
    no_of_days = models.CharField(max_length=500)
    total_expense = models.CharField(max_length=500)
    destinations = models.CharField(max_length=500)
    day_overview = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images', default=0)
    single_occupancy = models.IntegerField(default=0)
    twin_sharing = models.IntegerField(default=0)
    triple_sharing = models.IntegerField(default=0)
    infant = models.IntegerField(default=0)
    child_with_mat = models.IntegerField(default=0)
    child_without_mat = models.IntegerField(default=0)
    child = models.IntegerField(default=0)

    def __str__(self):
        return str(self.state)