# Generated by Django 3.1.5 on 2023-03-25 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_information', '0002_student_hall_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='hall_id',
        ),
        migrations.AddField(
            model_name='student',
            name='hall_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
