import json
from django.contrib.auth.models import User
from django.db import models

from wolf import data

class Solution(models.Model):
    code = models.CharField(max_length = 50000)
    tests = models.CharField(max_length = 50000)
    
    def getParsedTests(self):
        return data.Test.from_json_str(self.tests)
