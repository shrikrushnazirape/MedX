# Generated by Django 3.2.8 on 2021-10-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medecine',
            name='dose',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]