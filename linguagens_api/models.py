from django.db import models

class Linguagem(models.Model):

    title = models.CharField(max_length=30)
    url = models.CharField(max_length=200)
    ranking = models.IntegerField()

    def __str__(self):
        return self.title