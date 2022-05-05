from distutils.command.upload import upload
from django.db import models

# Create your models here.



class MediaFiles(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='img')
    css=models.FileField(upload_to='files')
    
    def __str__(self):
        return self.name