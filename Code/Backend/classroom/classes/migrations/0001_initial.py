# Generated by Django 3.2 on 2021-06-05 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_auto_20210501_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_code', models.CharField(max_length=20)),
                ('post', models.CharField(max_length=1000)),
                ('like_btn', models.BooleanField()),
                ('userID', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=1000)),
                ('userID', models.CharField(max_length=20)),
                ('postID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.post')),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_code', models.CharField(max_length=20)),
                ('class_pics', models.ImageField(blank=True, null=True, upload_to='')),
                ('course_title', models.CharField(max_length=20)),
                ('course_subtitle', models.CharField(max_length=20, null=True)),
                ('course_description', models.CharField(max_length=500, null=True)),
                ('fb_link', models.CharField(max_length=200, null=True)),
                ('discord_link', models.CharField(max_length=200, null=True)),
                ('facultyiD', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.faculty')),
            ],
        ),
    ]
