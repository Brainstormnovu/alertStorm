# Generated by Django 4.2.1 on 2023-05-22 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default='Nigeria', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='user',
            name='userid',
            field=models.CharField(default='<function uuid4 at 0x7fd0eed9d630>', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(default='Lagos', max_length=255),
        ),
    ]