# Generated by Django 4.2.3 on 2023-07-31 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_item_primary_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='characteristics',
            name='type',
            field=models.CharField(choices=[('string', 'String'), ('boolean', 'Boolean'), ('integer', 'Integer')], default='string', max_length=10),
        ),
    ]
