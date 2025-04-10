# Generated by Django 4.1.7 on 2025-04-06 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_transit', 'In_Transit'), ('delivered', 'Delivered')], max_length=20)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('delivery_date', models.DateTimeField(blank=True, null=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.buyer')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.driver')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='Vegetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vege_tracker.order')),
                ('vegetable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vege_tracker.vegetable')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='vegetables',
            field=models.ManyToManyField(through='vege_tracker.OrderItem', to='vege_tracker.vegetable'),
        ),
    ]
