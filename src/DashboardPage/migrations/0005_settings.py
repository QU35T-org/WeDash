# Generated by Django 3.2.9 on 2021-11-15 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DashboardPage', '0004_auto_20211114_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('dashboardID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DashboardPage.dashboard')),
            ],
        ),
    ]