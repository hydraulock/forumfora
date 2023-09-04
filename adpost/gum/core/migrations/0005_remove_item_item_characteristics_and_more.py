# Generated by Django 4.2.3 on 2023-07-24 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_characteristics_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_characteristics',
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_characteristics',
        ),
        migrations.CreateModel(
            name='Job_Characteristics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100)),
                ('characterictics', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.characteristics')),
                ('job', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.job')),
            ],
        ),
        migrations.CreateModel(
            name='Item_Characteristics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100)),
                ('characterictics', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.characteristics')),
                ('item', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='characteristics_item',
            field=models.ManyToManyField(through='core.Item_Characteristics', to='core.characteristics'),
        ),
        migrations.AddField(
            model_name='job',
            name='characteristics_job',
            field=models.ManyToManyField(through='core.Job_Characteristics', to='core.characteristics'),
        ),
    ]
