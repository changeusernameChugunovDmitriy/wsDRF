from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    annotation = models.TextField()
    author = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self):
        return self.title
