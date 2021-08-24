from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    email_id = models.EmailField(max_length=30)

    def __str__(self):
        return self.name