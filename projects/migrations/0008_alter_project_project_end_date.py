# Generated by Django 4.1.4 on 2023-01-01 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_project_options_project_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]