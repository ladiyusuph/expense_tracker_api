# Generated by Django 5.0.7 on 2024-08-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensetable',
            name='date',
            field=models.DateField(),
        ),
    ]
