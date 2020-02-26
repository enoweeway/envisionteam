# Generated by Django 3.0.3 on 2020-02-26 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20200226_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Radiology', 'Radiology'), ('Physical and Occupational Therapy', 'Physical and Occupational Therapy'), ('Neurology', 'Neurology'), ('Otology and Neurotology', 'Otology and Neurotology'), ('Nephrology', 'Nephrology'), ('Cardiology', 'Cardiology'), ('Gynecology & Urology', 'Gynecology & Urology'), ('Laboratory', 'Laboratory'), ('Sterilization', 'Sterilization'), ('Obstetrics and Maternity Care', 'Obstetrics and Maternity Care'), ('Apparel', 'Apparel'), ('Anaesthesiology', 'Anaesthesiology'), ('Dental E0quipment and Supplies', 'Dental Equipment and Supplies'), ('General Medical Equipment and Supplies', 'General Medical Equipment and Supplies'), ('Ophthalmology and Optometry', 'Ophthalmology and Optometry'), ('Surgery', 'Surgery')], max_length=100, null=True),
        ),
    ]
