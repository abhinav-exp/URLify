from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import uuid
from .helper import expiry_time_func
# Create your models here.

class Snippet(models.Model):
    link = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    creation_time = models.DateTimeField(default=datetime.now)
    expiry_time = models.DateTimeField(default = expiry_time_func)
    text = models.TextField()

class History(models.Model):
    snippet = models.ForeignKey(Snippet, on_delete = models.CASCADE)
    access_time = models.DateTimeField(default = datetime.now)
    ip = models.GenericIPAddressField()