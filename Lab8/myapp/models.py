from django.db import models

class Detail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    img = models.CharField(max_length=100)
