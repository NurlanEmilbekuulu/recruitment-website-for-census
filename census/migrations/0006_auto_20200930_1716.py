# Generated by Django 3.1.1 on 2020-09-30 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0005_auto_20200930_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Координатор'), (2, 'Инструктор'), (3, 'Каттоочу')], default=1, verbose_name='role'),
        ),
    ]
