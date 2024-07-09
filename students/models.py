from django.db import models


class StudentComplain(models.Model):
    name = models.CharField(max_length=20)
    body = models.TextField()

    def __str__(self):
        return self.name
