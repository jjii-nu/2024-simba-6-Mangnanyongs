# Generated by Django 5.0.6 on 2024-05-28 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_deadline_post_end_date_remove_post_day_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='scrap',
        ),
    ]
