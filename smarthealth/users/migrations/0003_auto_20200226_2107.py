# Generated by Django 3.0.3 on 2020-02-26 13:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200226_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='hospitalName',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='firstName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='lastName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='middleName',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
