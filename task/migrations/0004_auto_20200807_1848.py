# Generated by Django 2.2.15 on 2020-08-07 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_category_task_pool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_pool',
            name='mailbox_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='task_pool',
            name='message_id',
            field=models.CharField(max_length=500),
        ),
    ]
