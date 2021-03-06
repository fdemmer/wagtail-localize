# Generated by Django 3.0.6 on 2020-07-08 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtail_localize_translation', '0007_populate_translationsource_specific_content_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translationsource',
            name='specific_content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType'),
        ),
    ]
