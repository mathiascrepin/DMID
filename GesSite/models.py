from django.db import models
from django.db.models.fields.related import ForeignKey

class Teams(models.Model):
    members_name = models.CharField(max_length=200)
    posts = models.TextField()
    facebook = models.TextField()
    linkedin = models.TextField()
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    photo_image = models.CharField(max_length = 5000)
    photo_name = models.CharField(max_length=200)
    photo_description = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title


# Create your models here.
