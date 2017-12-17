# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-17 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='pythonsubtitle',
            name='detail',
            field=models.TextField(max_length=3000, verbose_name='\u8be6\u60c5'),
        ),
        migrations.AlterField(
            model_name='pythonsubtitle',
            name='sub_title',
            field=models.CharField(max_length=300, verbose_name='\u5b50\u7ae0\u8282\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='pythontitle',
            name='title',
            field=models.CharField(max_length=300, verbose_name='\u7ae0\u8282\u540d\u79f0'),
        ),
    ]