# Generated by Django 3.1.7 on 2021-05-20 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='location',
            new_name='favorite_food',
        ),
    ]