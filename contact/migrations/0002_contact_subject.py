# Generated by Django 5.0.1 on 2024-02-14 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='SOME STRINGS', max_length=100),
        ),
    ]
