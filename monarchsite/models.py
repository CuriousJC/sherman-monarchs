from django.db import models

class Monarch(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=200)
        path = models.CharField(max_length=200)
        aspect = models.CharField(max_length=200)

        def __str__(self):
                return f'{self.name} - Path of {self.path}'