# Generated by Django 3.1.7 on 2021-05-07 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='staticBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('drafter', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('textBody', models.TextField()),
            ],
        ),
    ]
