# Generated by Django 4.2.6 on 2025-05-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_post_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='userId',
            field=models.IntegerField(),
        ),
    ]
