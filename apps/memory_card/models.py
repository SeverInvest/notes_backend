

from django.db import models

# Create your models here.
from django.utils import timezone

from apps.users.models import User


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='results')
    created_at = models.DateTimeField(default=timezone.now)
    score = models.IntegerField()
    seconds = models.IntegerField()
