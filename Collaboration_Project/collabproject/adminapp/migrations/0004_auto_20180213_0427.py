# Generated by Django 2.0 on 2018-02-13 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_member_cohort'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='cohort',
            field=models.CharField(choices=[('Spring 2018', 'Spring 2018')], default=None, max_length=20),
        ),
    ]
