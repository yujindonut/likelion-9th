# Generated by Django 3.2.5 on 2021-08-17 16:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webtoonpage', '0004_auto_20210817_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='webtoonmodel',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
