# Generated by Django 2.2.1 on 2019-05-08 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price_div',
            field=models.CharField(default='class', max_length=500),
            preserve_default=False,
        ),
    ]