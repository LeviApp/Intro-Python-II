# Generated by Django 3.0.4 on 2020-03-06 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('murder_in_color', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='player',
        ),
        migrations.AddField(
            model_name='case',
            name='user_id',
            field=models.CharField(default='----', max_length=50),
            preserve_default=False,
        ),
    ]
