# Generated by Django 3.2.8 on 2022-06-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='film_ratings',
            field=models.FloatField(default=0, verbose_name='Рейтинг'),
        ),
    ]