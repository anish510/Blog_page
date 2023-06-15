from django.db import models
from datetime import datetime

# Create your models here.


class post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=10000000)
    image = models.ImageField(
        upload_to='static/images/demo/', blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
