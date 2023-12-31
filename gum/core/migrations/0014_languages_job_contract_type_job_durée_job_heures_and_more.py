# Generated by Django 4.2.3 on 2023-08-01 09:52

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_characteristics_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
            ],
            options={
                'verbose_name': 'Langues',
            },
        ),
        migrations.AddField(
            model_name='job',
            name='contract_type',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='job',
            name='durée',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='job',
            name='heures',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='job',
            name='job_logo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=core.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='job',
            name='website',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='langues',
            field=models.ManyToManyField(default=None, to='core.languages'),
        ),
    ]
