# Generated by Django 4.1 on 2023-02-19 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("partygame", "0002_category2_category3_category4"),
    ]

    operations = [
        migrations.AddField(
            model_name="partygamepost",
            name="category2",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="partygame.category2",
                verbose_name="カテゴリ2",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="partygamepost",
            name="category3",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="partygame.category3",
                verbose_name="カテゴリ3",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="partygamepost",
            name="category4",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="partygame.category4",
                verbose_name="カテゴリ4",
            ),
            preserve_default=False,
        ),
    ]