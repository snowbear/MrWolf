from django.contrib.auth.models import User
from django.db import models

class Solution(models.Model):
    code = models.CharField(max_length = 50000)
    tests = models.CharField(max_length = 50000)