# Generated by Django 2.2.1 on 2019-05-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extra',
            name='extra_id',
        ),
        migrations.RemoveField(
            model_name='ramen',
            name='ramen_id',
        ),
        migrations.RemoveField(
            model_name='topping',
            name='topping_id',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='age',
            field=models.IntegerField(default=1),
        ),
    ]
