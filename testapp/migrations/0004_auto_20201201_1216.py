# Generated by Django 3.0.8 on 2020-12-01 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
