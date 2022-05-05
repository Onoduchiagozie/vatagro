# Generated by Django 4.0.4 on 2022-05-04 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='farmername',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='goods.merchant'),
        ),
        migrations.AlterField(
            model_name='product',
            name='inter_state_shipping_fee',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='intra_state_shipping_fee',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='store_location',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='goods.storelocation'),
        ),
    ]