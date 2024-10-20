# Generated by Django 2.2 on 2020-06-09 16:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0022_remove_author_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='user_post',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='answers',
                to='forum.UserPost'),
        ),
    ]
