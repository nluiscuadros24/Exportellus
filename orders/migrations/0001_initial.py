# Generated by Django 3.0.7 on 2020-06-24 21:51

from django.db import migrations, models
import django.db.models.deletion
import orders.common


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing_profiles', '0001_initial'),
        ('promo_codes', '0001_initial'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100, unique=True)),
                ('status', models.CharField(choices=[(orders.common.OrderStatus['CREATED'], 'CREATED'), (orders.common.OrderStatus['PAYED'], 'PAYED'), (orders.common.OrderStatus['COMPLETED'], 'COMPLETED'), (orders.common.OrderStatus['CANCELED'], 'CANCELED')], default=orders.common.OrderStatus['CREATED'], max_length=50)),
                ('shipping_total', models.DecimalField(decimal_places=2, default=5, max_digits=8)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('billing_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billing_profiles.BillingProfile')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.Cart')),
                ('promo_code', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='promo_codes.PromoCode')),
            ],
        ),
    ]
