# Generated by Django 4.0 on 2022-01-04 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_alter_task_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]