from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import uuid
# Create your models here.
class Snippet(models.Model):
    link = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    creation_time = models.DateTimeField(default=datetime.now)
    text = models.TextField()
