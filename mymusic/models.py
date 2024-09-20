from django.db import models

# Create your models here.
class AddedMusic(models.Model):
  title = models.CharField(max_length=200)
  singer = models.CharField(max_length=200)
  album = models.CharField(max_length=200)
  albumimg = models.FileField("album_image", upload_to="uploads/", max_length=300)
  feeling = models.CharField(max_length=100)
  memo = models.TextField()