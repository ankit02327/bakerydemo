# Generated by Django 4.2.13 on 2024-10-24 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0021_alter_footertext_locale"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="genericsettings",
            name="twitter_url",
        ),
        migrations.AddField(
            model_name="genericsettings",
            name="mastodon_url",
            field=models.URLField(blank=True, verbose_name="Mastodon URL"),
        ),
    ]
