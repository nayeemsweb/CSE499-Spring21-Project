# Generated by Django 3.1.7 on 2021-06-14 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0007_classroom_class_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classroom',
            old_name='facultyiD',
            new_name='faculty',
        ),
    ]
