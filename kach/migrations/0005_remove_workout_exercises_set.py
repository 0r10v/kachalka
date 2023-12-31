# Generated by Django 4.2 on 2023-06-03 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kach', '0004_workout_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='exercises',
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repetitions', models.PositiveIntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kach.exercise')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sets', to='kach.workout')),
            ],
        ),
    ]
