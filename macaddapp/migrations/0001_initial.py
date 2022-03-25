# Generated by Django 3.2.4 on 2022-03-07 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ftp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac', models.CharField(default='', max_length=500)),
                ('username', models.CharField(max_length=200)),
                ('companyname', models.CharField(default='abc', max_length=200)),
                ('security_key', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('address', models.TextField(max_length=500, null=True)),
            ],
        ),
    ]
