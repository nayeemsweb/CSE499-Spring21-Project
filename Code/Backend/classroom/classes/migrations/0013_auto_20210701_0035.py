# Generated by Django 3.1.7 on 2021-06-30 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0012_student_classroom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='class_code',
            new_name='classroom',
        ),
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='classes.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='userID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
