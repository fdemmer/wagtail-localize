# Generated by Django 2.2.9 on 2020-01-06 12:27

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail_localize.test.models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtail_localize_test", "0006_testnonparentalchildobject"),
    ]

    operations = [
        migrations.RenameField(
            model_name="testpage",
            old_name="test_synchronizedfield",
            new_name="test_synchronized_textfield",
        ),
        migrations.AddField(
            model_name="testpage",
            name="test_synchronized_charfield",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="testpage",
            name="test_synchronized_customfield",
            field=wagtail_localize.test.models.TestCustomField(blank=True),
        ),
        migrations.AddField(
            model_name="testpage",
            name="test_synchronized_emailfield",
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name="testpage",
            name="test_synchronized_richtextfield",
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name="testpage",
            name="test_synchronized_slugfield",
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name="testpage",
            name="test_synchronized_snippet",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtail_localize_test.TestSnippet",
            ),
        ),
        migrations.AddField(
            model_name="testpage",
            name="test_synchronized_streamfield",
            field=wagtail.core.fields.StreamField(
                [
                    ("test_charblock", wagtail.core.blocks.CharBlock(max_length=255)),
                    ("test_textblock", wagtail.core.blocks.TextBlock()),
                    ("test_emailblock", wagtail.core.blocks.EmailBlock()),
                    ("test_urlblock", wagtail.core.blocks.URLBlock()),
                    ("test_richtextblock", wagtail.core.blocks.RichTextBlock()),
                    ("test_rawhtmlblock", wagtail.core.blocks.RawHTMLBlock()),
                    ("test_blockquoteblock", wagtail.core.blocks.BlockQuoteBlock()),
                    (
                        "test_structblock",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("field_a", wagtail.core.blocks.TextBlock()),
                                ("field_b", wagtail.core.blocks.TextBlock()),
                            ]
                        ),
                    ),
                    (
                        "test_listblock",
                        wagtail.core.blocks.ListBlock(wagtail.core.blocks.TextBlock()),
                    ),
                    (
                        "test_nestedstreamblock",
                        wagtail.core.blocks.StreamBlock(
                            [
                                ("block_a", wagtail.core.blocks.TextBlock()),
                                ("block_b", wagtail.core.blocks.TextBlock()),
                            ]
                        ),
                    ),
                    (
                        "test_customstructblock",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("field_a", wagtail.core.blocks.TextBlock()),
                                ("field_b", wagtail.core.blocks.TextBlock()),
                            ]
                        ),
                    ),
                ],
                blank=True,
            ),
        ),
        migrations.AddField(
            model_name="testpage",
            name="test_synchronized_urlfield",
            field=models.URLField(blank=True),
        ),
        migrations.CreateModel(
            name="TestSynchronizedChildObject",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("field", models.TextField()),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="test_synchronized_childobjects",
                        to="wagtail_localize_test.TestPage",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False},
        ),
    ]
