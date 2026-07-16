from django.db import models

# Create your models here.

class register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    message = models.TextField(blank=True)
    is_new = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
