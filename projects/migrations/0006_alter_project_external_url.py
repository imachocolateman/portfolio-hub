# Generated by Django 4.0.3 on 2022-04-10 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='external_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]