from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    times_used = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def increment_times_used(self):
        self.times_used += 1
        self.save()