# Generated by Django 4.2.3 on 2023-07-27 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_phonenumber_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item_characteristics',
            old_name='characterictics',
            new_name='characteristics',
        ),
    ]
