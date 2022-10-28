from django.db import models


class prods(models.Model):
    ref = models.CharField(max_length=180)
    zipcode = models.IntegerField()
    store = models.CharField(max_length=90)
    amount = models.FloatField()

    def __str__(self):
        return self.ref


class coordsprods(models.Model):
    lat = models.FloatField()
    long = models.FloatField()
    prods = models.ForeignKey(prods, on_delete=models.CASCADE)

    def __str__(self):
        return self.lat
