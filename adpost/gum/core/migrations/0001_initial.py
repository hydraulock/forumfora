# Generated by Django 4.2.3 on 2023-07-24 14:04

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('description', models.TextField(default=None)),
                ('available', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Annonce',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
        ),
        migrations.CreateModel(
            name='TypeJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('subcategory', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Characteristics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default=None, max_length=500)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.category')),
                ('subcategory', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.subcategory')),
            ],
            options={
                'verbose_name': 'Caractéristique',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('ad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.ad')),
                ('salary', models.IntegerField(default=None)),
                ('job_characteristics', models.ManyToManyField(to='core.characteristics')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.typejob')),
            ],
            options={
                'verbose_name': 'Job',
            },
            bases=('core.ad',),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('ad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.ad')),
                ('price', models.IntegerField(default=None)),
                ('product_image1', models.ImageField(blank=True, null=True, upload_to=core.models.user_directory_path)),
                ('product_image2', models.ImageField(blank=True, null=True, upload_to=core.models.user_directory_path)),
                ('product_image3', models.ImageField(blank=True, null=True, upload_to=core.models.user_directory_path)),
                ('product_image4', models.ImageField(blank=True, null=True, upload_to=core.models.user_directory_path)),
                ('product_image5', models.ImageField(blank=True, null=True, upload_to=core.models.user_directory_path)),
                ('product_image6', models.ImageField(blank=True, null=True, upload_to=core.models.user_directory_path)),
                ('product_image7', models.ImageField(blank=True, null=True, upload_to=core.models.user_directory_path)),
                ('product_image8', models.ImageField(blank=True, null=True, upload_to=core.models.user_directory_path)),
                ('product_image9', models.ImageField(blank=True, null=True, upload_to=core.models.user_directory_path)),
                ('product_image10', models.ImageField(blank=True, null=True, upload_to=core.models.user_directory_path)),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.category')),
                ('item_characteristics', models.ManyToManyField(to='core.characteristics')),
                ('subcategory', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.subcategory')),
            ],
            options={
                'verbose_name': 'Produit',
            },
            bases=('core.ad',),
        ),
    ]
