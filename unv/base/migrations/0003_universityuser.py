# Generated by Django 5.0.3 on 2024-04-05 14:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_useraccount_is_student_useraccount_is_university_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityUser',
            fields=[
                ('useraccount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('universityname', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('base.useraccount',),
        ),
    ]
