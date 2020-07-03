# Generated by Django 2.1.15 on 2020-07-03 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtail_localize_translation', '0012_object_path_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='translationsource',
            name='specific_content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType'),
        ),
    ]