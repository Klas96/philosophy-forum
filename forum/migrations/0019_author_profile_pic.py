# Generated by Django 2.2 on 2020-05-30 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0018_answer_downvotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='profile_pic',
            field=models.ImageField(
                blank=True,
                default='default_pro_pic.png',
                null=True,
                upload_to=''),
        ),
    ]
