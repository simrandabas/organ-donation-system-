# Generated by Django 5.1.1 on 2024-11-06 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donors',
            name='address',
            field=models.TextField(verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='donors',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3, verbose_name='Blood Group'),
        ),
        migrations.AlterField(
            model_name='donors',
            name='contact_number',
            field=models.CharField(max_length=15, verbose_name='Contact Number'),
        ),
        migrations.AlterField(
            model_name='donors',
            name='date_of_birth',
            field=models.DateField(verbose_name='Date of birth'),
        ),
        migrations.AlterField(
            model_name='donors',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='donors',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='donors',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='donors',
            name='organ_to_donate',
            field=models.CharField(max_length=255, verbose_name='Organ to donate'),
        ),
    ]
