from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to='media/')
    description = models.TextField()

    def __str__(self):
        return self.title
