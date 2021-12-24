# Generated by Django 3.2.9 on 2021-12-24 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seasapp', '0020_alter_course_t_credithour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_t',
            name='courseID',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course_t',
            name='courseName',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='faculty_t',
            name='facultyID',
            field=models.CharField(max_length=7, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='room_t',
            name='roomID',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='section_t',
            name='day',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
