from django.db import models

# Create your models here.
class Material(models.Model):
    number = models.CharField(max_length=40)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
