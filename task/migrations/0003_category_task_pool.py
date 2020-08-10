# Generated by Django 2.2.15 on 2020-08-07 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0002_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='task_pool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_attachment_id', models.IntegerField(default=0)),
                ('mailbox_id', models.CharField(max_length=500)),
                ('subject', models.CharField(max_length=500)),
                ('message_id', models.IntegerField(default=0)),
                ('in_reply_to_id', models.IntegerField(default=0, null=True)),
                ('from_header', models.CharField(max_length=500)),
                ('to_header', models.CharField(max_length=500)),
                ('outgoing', models.BooleanField(default=False)),
                ('body', models.TextField(blank=True, null=True)),
                ('encoded', models.BooleanField(default=False)),
                ('processed', models.DateTimeField(auto_now_add=True)),
                ('read', models.DateTimeField(auto_now_add=True)),
                ('eml', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.category')),
                ('mail_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]