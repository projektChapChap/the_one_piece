from django.db import models


class Post(models.Model):
    tarehe = models.CharField(max_length=200)
    jina = models.CharField(max_length=200)
    maelezo = models.CharField(max_length=200)
    mmuda = models.TimeField()
    picha = models.ImageField(upload_to='uploads/', blank=True)
    
    def __str__(self):
        return self.jina
    