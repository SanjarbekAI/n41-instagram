# Generated by Django 5.0.6 on 2024-07-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storymodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]