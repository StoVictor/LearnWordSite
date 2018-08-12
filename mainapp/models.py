from django.db import models
from django.contrib.auth.models import User


class WordPack:
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    words = models.TextField()