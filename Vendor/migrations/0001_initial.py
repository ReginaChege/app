# Generated by Django 4.2.1 on 2023-06-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('second_name', models.CharField(max_length=32)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=32)),
            ],
        ),
    ]
