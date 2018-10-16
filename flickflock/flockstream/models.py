from django.db import models
from django.conf import settings


class Photo(models.Model):
    photo = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50, default="dis photo")
    published_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)
    # Date Posted

    def __str__(self):
        return self.title
