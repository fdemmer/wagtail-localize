# Generated by Django 2.1.15 on 2020-06-27 11:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_localize', '0006_delete_language_model'),
        ('wagtail_localize_translation', '0004_translationrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translationrequest',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='translationrequest',
            unique_together={('source', 'target_locale')},
        ),
    ]