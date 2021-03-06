# Generated by Django 3.2.9 on 2021-11-15 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('ticket_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('subject', models.CharField(max_length=20)),
                ('message', models.TextField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
    ]
