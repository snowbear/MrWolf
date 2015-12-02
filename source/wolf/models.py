from django.db import models

from wolf import data


class Language(models.Model):
    name = models.CharField(max_length=20)
    version = models.CharField(max_length=200)
    hr_code = models.IntegerField(null=False)

    def __str__(self):
        return self.name


class Template(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50000)
    language = models.ForeignKey(Language, null=False)
    
    def __str__(self):
        return self.name


class Solution(models.Model):
    code = models.CharField(max_length=50000)
    tests = models.CharField(max_length=50000)
    language = models.ForeignKey(Language, null=False)
    
    def getParsedTests(self):
        return data.Test.from_json_str(self.tests)
