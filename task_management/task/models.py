from django.db import models

class Task(models.Model):
    title = models.CharField(null=True, max_length=20)
    description = models.TextField()
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title