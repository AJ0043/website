from django.db import models

class Contact(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Phone = models.CharField(max_length=200)
    Business = models.CharField(max_length=200)
    Service = models.CharField(max_length=200)
    Message = models.TextField()

    def __str__(self):
        return self.Name