# Generated by Django 4.1 on 2023-05-02 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Authapp', '0001_initial'),
        ('Vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_paid', models.BooleanField(default=False)),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authapp.customers')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_email', models.CharField(max_length=50, unique=True)),
                ('contact_message', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.CharField(max_length=12, unique=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authapp.customers')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('points', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vendor.games')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.orders')),
            ],
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.cart')),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Vendor.games')),
            ],
        ),
    ]
