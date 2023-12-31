# Generated by Django 4.2.3 on 2023-08-01 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_delete_typejob'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='job',
            name='langues',
            field=models.ManyToManyField(blank=True, default=None, to='core.languages'),
        ),
        migrations.AlterField(
            model_name='job',
            name='niveau',
            field=models.ManyToManyField(blank=True, default=None, to='core.niveau'),
        ),
    ]
