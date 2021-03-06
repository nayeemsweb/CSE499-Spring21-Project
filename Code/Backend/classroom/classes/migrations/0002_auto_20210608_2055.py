# Generated by Django 3.1.7 on 2021-06-08 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='discord_link',
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='fb_link',
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='like_btn',
        ),
        migrations.AlterField(
            model_name='classroom',
            name='class_code',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='class_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.classroom'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='postID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
