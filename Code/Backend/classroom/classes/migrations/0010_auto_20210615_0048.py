# Generated by Django 3.1.7 on 2021-06-14 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0009_auto_20210615_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='class_code',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
    ]