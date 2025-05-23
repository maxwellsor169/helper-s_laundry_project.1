# Generated by Django 5.1.7 on 2025-04-03 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_type', models.CharField(max_length=200)),
                ('specification', models.TextField()),
                ('machine_no', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('status', models.IntegerField(choices=[(0, 'Taken'), (1, 'Available')], default=0)),
            ],
        ),
    ]
