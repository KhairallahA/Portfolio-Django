# Generated by Django 3.1.4 on 2021-03-20 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
