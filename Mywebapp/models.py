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
    


class PythonTopic(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150, null=True, blank=True)  # Allow NULL values
    content1 = models.TextField()
    content2 = models.TextField(null=True, blank=True)
    content3 = models.TextField(null=True, blank=True)
    content4 = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
