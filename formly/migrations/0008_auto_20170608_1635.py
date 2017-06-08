# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-08 16:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formly', '0007_help_text_and_label_to_textfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdinalScale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(choices=[('likert', 'Likert Scale'), ('rating', 'Rating Scale')], max_length=6)),
            ],
        ),
        migrations.RenameModel(
            old_name='LikertChoice',
            new_name='OrdinalChoice',
        ),
        migrations.AlterField(
            model_name='field',
            name='field_type',
            field=models.IntegerField(choices=[(0, 'Free Response - One Line'), (1, 'Free Response - Box'), (2, 'Multiple Choice - Pick One'), (4, 'Multiple Choice - Pick One (Dropdown)'), (5, 'Multiple Choice - Can select multiple answers'), (3, 'Date'), (6, 'File Upload'), (7, 'True/False'), (8, 'Multiple Free Responses - Single Lines'), (9, 'Likert Scale'), (10, 'Rating Scale')]),
        ),
        migrations.AlterField(
            model_name='field',
            name='scale',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='formly.OrdinalScale'),
        ),
        migrations.AlterField(
            model_name='ordinalchoice',
            name='scale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='formly.OrdinalScale'),
        ),
        migrations.DeleteModel(
            name='LikertScale',
        ),
    ]
