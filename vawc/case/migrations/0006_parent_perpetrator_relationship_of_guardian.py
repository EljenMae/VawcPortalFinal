# Generated by Django 5.0.1 on 2024-03-24 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0005_parent_relationship_to_victim_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent_perpetrator',
            name='relationship_of_guardian',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
