# Generated by Django 4.2 on 2023-04-30 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikefit', '0002_medidas_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medidas',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]