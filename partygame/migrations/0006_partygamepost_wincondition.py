# Generated by Django 4.1 on 2023-03-06 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("partygame", "0005_partygamepost_item_alter_partygamepost_preparation"),
    ]

    operations = [
        migrations.AddField(
            model_name="partygamepost",
            name="wincondition",
            field=models.CharField(default=1, max_length=100, verbose_name="勝利条件を一言で"),
            preserve_default=False,
        ),
    ]