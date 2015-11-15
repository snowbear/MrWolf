import json
from django.db import models

from wolf import data

class Template(models.Model):
    name = models.CharField(max_length = 100)
    code = models.CharField(max_length = 50000)
    
    def __str__(self):
        return self.name

class Solution(models.Model):
    code = models.CharField(max_length = 50000)
    tests = models.CharField(max_length = 50000)
    
    def getParsedTests(self):
        return data.Test.from_json_str(self.tests)
