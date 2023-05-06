# Generated by Django 4.2 on 2023-05-01 20:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikefit', '0004_rename_medidas_modelcalculos'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelMural',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.TextField()),
                ('nome', models.TextField()),
                ('email', models.TextField()),
                ('data', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
