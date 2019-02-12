from django.db import models
from datetime import datetime

# Create your models here.


class TodoItem(models.Model):
    content = models.TextField()
    published = models.DateTimeField("date published", default=datetime.now())
