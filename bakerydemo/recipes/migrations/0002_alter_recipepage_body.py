# Generated by Django 6.0.dev20250116121251 on 2025-02-11 16:44

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipepage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("heading_block", 2),
                    ("paragraph_block", 3),
                    ("block_quote", 6),
                    ("table_block", 7),
                    ("typed_table_block", 12),
                    ("image_block", 13),
                    ("embed_block", 14),
                    ("ingredients_list", 16),
                    ("steps_list", 19),
                ],
                blank=True,
                block_lookup={
                    0: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {"form_classname": "title", "required": True},
                    ),
                    1: (
                        "wagtail.blocks.ChoiceBlock",
                        [],
                        {
                            "blank": True,
                            "choices": [
                                ("", "Select a header size"),
                                ("h2", "H2"),
                                ("h3", "H3"),
                                ("h4", "H4"),
                            ],
                            "required": False,
                        },
                    ),
                    2: (
                        "wagtail.blocks.StructBlock",
                        [[("heading_text", 0), ("size", 1)]],
                        {"group": "Content"},
                    ),
                    3: (
                        "wagtail.blocks.RichTextBlock",
                        (),
                        {
                            "group": "Content",
                            "icon": "pilcrow",
                            "template": "blocks/paragraph_block.html",
                        },
                    ),
                    4: ("wagtail.blocks.TextBlock", (), {}),
                    5: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {"blank": True, "label": "e.g. Mary Berry", "required": False},
                    ),
                    6: (
                        "wagtail.blocks.StructBlock",
                        [[("text", 4), ("attribute_name", 5)]],
                        {"group": "Content"},
                    ),
                    7: (
                        "wagtail.contrib.table_block.blocks.TableBlock",
                        (),
                        {"group": "Content"},
                    ),
                    8: ("wagtail.blocks.CharBlock", (), {}),
                    9: ("wagtail.blocks.FloatBlock", (), {}),
                    10: ("wagtail.blocks.RichTextBlock", (), {}),
                    11: ("wagtail.images.blocks.ImageBlock", [], {}),
                    12: (
                        "wagtail.contrib.typed_table_block.blocks.TypedTableBlock",
                        [
                            [
                                ("text", 8),
                                ("numeric", 9),
                                ("rich_text", 10),
                                ("image", 11),
                            ]
                        ],
                        {"group": "Content"},
                    ),
                    13: ("wagtail.images.blocks.ImageBlock", [], {"group": "Media"}),
                    14: (
                        "wagtail.embeds.blocks.EmbedBlock",
                        (),
                        {
                            "group": "Media",
                            "help_text": "Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks",
                            "icon": "media",
                            "template": "blocks/embed_block.html",
                        },
                    ),
                    15: (
                        "wagtail.blocks.RichTextBlock",
                        (),
                        {"features": ["bold", "italic", "link"]},
                    ),
                    16: (
                        "wagtail.blocks.ListBlock",
                        (15,),
                        {
                            "group": "Cooking",
                            "icon": "list-ol",
                            "max_num": 10,
                            "min_num": 2,
                        },
                    ),
                    17: (
                        "wagtail.blocks.ChoiceBlock",
                        [],
                        {"choices": [("S", "Small"), ("M", "Medium"), ("L", "Large")]},
                    ),
                    18: (
                        "wagtail.blocks.StructBlock",
                        [[("text", 15), ("difficulty", 17)]],
                        {},
                    ),
                    19: (
                        "wagtail.blocks.ListBlock",
                        (18,),
                        {
                            "group": "Cooking",
                            "icon": "tasks",
                            "max_num": 10,
                            "min_num": 2,
                        },
                    ),
                },
                help_text="The recipe’s step-by-step instructions and any other relevant information.",
            ),
        ),
    ]
