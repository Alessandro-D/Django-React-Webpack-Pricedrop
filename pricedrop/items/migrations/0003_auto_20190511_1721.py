# Generated by Django 2.2.1 on 2019-05-11 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_item_price_div'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price_div',
            field=models.CharField(default='default', max_length=500),
        ),
    ]
