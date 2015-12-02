# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wolf', '0002_template'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('version', models.CharField(max_length=200)),
                ('hr_code', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='solution',
            name='language',
            field=models.ForeignKey(default=None, to='wolf.Language'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='template',
            name='language',
            field=models.ForeignKey(default=None, to='wolf.Language'),
            preserve_default=False,
        ),
    ]
