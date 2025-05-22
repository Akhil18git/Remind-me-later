from django.db import models
from django.utils import timezone

class Message(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} {self.time}: {self.message} {self.created_at}"