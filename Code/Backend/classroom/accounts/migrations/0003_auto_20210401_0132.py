# Generated by Django 3.1.7 on 2021-03-31 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210330_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facultyprofile',
            name='department',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='department',
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.CharField(choices=[('Accounting & Finance', 'Accounting & Finance'), ('Economics', 'Economics'), ('Management', 'Management'), ('Marketing & International Business', 'Marketing & International Business'), ('MBA & EMBA Programs', 'MBA & EMBA Programs'), ('Architecture', 'Architecture'), ('Civil & Environmental Engineering', 'Civil & Environmental Engineering'), ('Electrical & Computer Engineering', 'Electrical & Computer Engineering'), ('Mathematics & Physics', 'Mathematics & Physics'), ('English & Modern Languages', 'English & Modern Languages'), ('Political Science & Sociology', 'Political Science & Sociology'), ('Law', 'Law'), ('Biochemistry & Microbiology', 'Biochemistry & Microbiology'), ('Environmental Science & Management', 'Environmental Science & Management'), ('Pharmaceutical Sciences', 'Pharmaceutical Sciences'), ('Public Health', 'Public Health')], default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='is_faculty',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='facultyprofile',
            name='facultyID',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='facultyprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='studentID',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]