# Generated by Django 4.1.5 on 2023-01-12 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_routine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diet', models.CharField(max_length=50)),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.workout')),
            ],
        ),
    ]
