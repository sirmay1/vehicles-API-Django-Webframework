from django.db import models


class Travel(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.make + ' | ' + self.model + ' | ' + self.color + ' | ' + str(self.year)
