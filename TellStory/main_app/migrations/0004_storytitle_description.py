# Generated by Django 4.1.3 on 2022-12-07 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_storytitle_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='storytitle',
            name='description',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
