# Generated by Django 4.2 on 2023-06-03 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kach', '0003_exercise_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
