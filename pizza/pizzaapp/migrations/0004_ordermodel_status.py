# Generated by Django 3.2.4 on 2021-06-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0003_ordermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(default='pending', max_length=10),
            preserve_default=False,
        ),
    ]