# Generated by Django 5.0.1 on 2024-03-29 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0009_merge_20240324_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='witness',
            name='email',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
