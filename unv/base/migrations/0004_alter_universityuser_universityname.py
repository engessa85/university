# Generated by Django 5.0.3 on 2024-04-05 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_universityuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universityuser',
            name='universityname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]