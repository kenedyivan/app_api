# Generated by Django 2.0.2 on 2018-02-26 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vecurityapiapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('account_number', models.CharField(max_length=200)),
                ('account_name', models.CharField(max_length=200)),
                ('nin', models.CharField(max_length=200)),
                ('dob', models.DateField(verbose_name='date of birth')),
                ('gender', models.CharField(max_length=200)),
                ('profile_photo', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(editable=False, verbose_name='date created')),
                ('updated_at', models.DateTimeField(verbose_name='date updated')),
            ],
        ),
    ]
