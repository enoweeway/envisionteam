# Generated by Django 3.0.3 on 2020-02-26 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20200226_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Otology and Neurotology', 'Otology and Neurotology'), ('Neurology', 'Neurology'), ('Dental E0quipment and Supplies', 'Dental Equipment and Supplies'), ('Physical and Occupational Therapy', 'Physical and Occupational Therapy'), ('Anaesthesiology', 'Anaesthesiology'), ('Laboratory', 'Laboratory'), ('Nephrology', 'Nephrology'), ('Radiology', 'Radiology'), ('Ophthalmology and Optometry', 'Ophthalmology and Optometry'), ('Cardiology', 'Cardiology'), ('General Medical Equipment and Supplies', 'General Medical Equipment and Supplies'), ('Surgery', 'Surgery'), ('Apparel', 'Apparel'), ('Gynecology & Urology', 'Gynecology & Urology'), ('Sterilization', 'Sterilization'), ('Obstetrics and Maternity Care', 'Obstetrics and Maternity Care')], max_length=100, null=True),
        ),
    ]
