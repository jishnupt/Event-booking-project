from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=50)
    location = models.TextField(null=True)
    date = models.DateField(null=True)
    total_seats = models.PositiveIntegerField(null=True)
    available_seats = models.PositiveIntegerField(null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.available_seats = self.total_seats
        super().save(*args, **kwargs)
