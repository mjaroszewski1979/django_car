# Generated by Django 4.0.4 on 2022-05-24 18:06

from django.db import migrations, models
import django.db.models.functions.text


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producer', models.CharField(max_length=128)),
                ('country_of_origin', models.CharField(max_length=128)),
                ('year_of_production', models.PositiveIntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='car_photos/')),
            ],
            options={
                'ordering': [django.db.models.functions.text.Lower('producer')],
            },
        ),
    ]
