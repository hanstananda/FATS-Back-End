# Generated by Django 3.1 on 2020-09-07 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_server', '0006_auto_20200902_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance_server.courseclass')),
                ('students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance_server.studentprofile')),
            ],
        ),
    ]
