# Generated by Django 3.1.1 on 2020-10-01 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0007_auto_20201001_1527'),
        ('accounts', '0002_auto_20201001_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='raw_password',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='сырсөз'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='district',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='census.district', verbose_name='район'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Администрация'), (2, 'Модератор')], default=1, verbose_name='ролу'),
        ),
    ]
