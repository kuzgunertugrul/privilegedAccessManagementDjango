# Generated by Django 3.2.9 on 2021-11-22 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_delete_authenticationtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthenticationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authenticationName', models.CharField(max_length=100)),
                ('ls', models.BooleanField()),
                ('cd', models.BooleanField()),
            ],
        ),
    ]
