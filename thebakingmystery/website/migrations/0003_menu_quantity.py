# Generated by Django 3.0.8 on 2020-09-29 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200927_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='quantity',
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
    ]