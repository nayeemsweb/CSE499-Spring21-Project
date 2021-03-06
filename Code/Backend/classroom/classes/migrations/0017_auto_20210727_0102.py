# Generated by Django 3.1.7 on 2021-07-26 19:02

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0016_exam_student_exam'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_input', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('obtained_marks', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='student_exam',
        ),
        migrations.AlterField(
            model_name='classtime',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student_classroom',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='student_submission',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.exam'),
        ),
    ]
