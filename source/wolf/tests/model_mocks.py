from django.db.models import *

from wolf import models


def mock_language():
    next_code = 1
    if models.Language.objects.all().count() > 0:
        next_code = models.Language.objects.all().aggregate(Max('hr_code'))['hr_code__max'] + 1
    return models.Language.objects.create(hr_code=next_code)


def mock_template():
    language = mock_language()
    return models.Template.objects.create(language=language)


def mock_solution():
    language = mock_language()
    return models.Solution.objects.create(
        language=language,
    )
