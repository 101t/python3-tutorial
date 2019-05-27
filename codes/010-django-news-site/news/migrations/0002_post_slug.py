# Generated by Django 2.2.1 on 2019-05-25 09:25

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='title', unique_with=['title']),
            preserve_default=False,
        ),
    ]
