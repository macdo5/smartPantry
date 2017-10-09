# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-07 03:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pantry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now)),
                ('columns', models.IntegerField()),
                ('rows', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PantryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='pantryImages')),
                ('column', models.IntegerField()),
                ('row', models.IntegerField()),
                ('pantry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pantry.Pantry')),
            ],
        ),
        migrations.CreateModel(
            name='WeightedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=200)),
                ('grams', models.IntegerField()),
                ('pantry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pantry.Pantry')),
            ],
        ),
    ]
