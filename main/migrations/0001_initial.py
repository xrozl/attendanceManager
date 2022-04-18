# Generated by Django 4.0.4 on 2022-04-18 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=64)),
                ('user_fullname', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('user_id', models.IntegerField(default=0)),
            ],
        ),
    ]
