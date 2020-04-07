from django.apps import AppConfig


class WagtailLocalizeDeepLAppConfig(AppConfig):
    label = "wagtail_localize_deepl"
    name = "wagtail_localize.translation.engines.deepl"
    verbose_name = "Wagtail Localize DeepL translation engine"
