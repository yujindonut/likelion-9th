# Generated by Django 3.2.6 on 2021-08-24 18:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tripinfo', '0002_alter_writeinfomodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='writeinfomodel',
            name='followers',
            field=models.ManyToManyField(related_name='followings', to=settings.AUTH_USER_MODEL),
        ),
    ]
