# Generated by Django 3.2.10 on 2022-01-09 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_shop_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='shop_type',
            field=models.CharField(choices=[('SUP', 'Supermarket'), ('HYP', 'Hypermarket'), ('BAKERY', 'Bakery'), ('FRUIT', 'fruit store'), ('BOOKSHOP', 'Bookshop')], default='SUP', max_length=17),
        ),
    ]
