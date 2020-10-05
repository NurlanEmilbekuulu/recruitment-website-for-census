# Generated by Django 3.1.1 on 2020-09-30 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0003_auto_20200930_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[(1, 'Координатор'), (2, 'Инструктор'), (3, 'Каттоочу')], max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Орнотуулар',
                'verbose_name_plural': 'Орнотуулар',
            },
        ),
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Координатор'), (2, 'Инструктор'), (3, 'Каттоочу')], default=1, verbose_name='role'),
        ),
    ]