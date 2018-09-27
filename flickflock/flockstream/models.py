from django.conf import settings
from django.db import models


class Photo(models.Model):
    photo = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50, default="dis photo")
    # published_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # TO DO: public or private
